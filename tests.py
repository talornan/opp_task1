import unittest

from Building import Building
from Calls import Calls
from offlineAlgo import OfflineAlgo


class MyTestCase(unittest.TestCase):
    def test_building(self):
        building = Building("resources/B1.json")
        self.assertEqual(building.getMaxFloor(), 10)
        self.assertEqual(building.getMinFloor(), -2)
        self.assertEqual(building.getNumberOfElevetor(), 1)  # add assertion here
    def test_elevator(self):
        building = Building("resources/B1.json")
        elevator = building.getElevator(0)
        self.assertEqual(elevator.getId(), 0)
        self.assertEqual(elevator.getMinFloor(), -2)
        self.assertEqual(elevator.getMaxFloor(), 10)
        self.assertEqual(elevator.getSpeed(), 0.5)
        self.assertEqual(elevator.getOpenTime(), 2)
        self.assertEqual(elevator.getStopTime(), 3.0)
        self.assertEqual(elevator.getPosition(), 0)
        self.assertEqual(elevator.getStartTime(), 3)


    def test_call(self):
        calls = Calls("resources/Calls_a.csv")
        self.assertEqual(len(calls.calls), 100)
        call = calls.calls[0]
        self.assertEqual(call.getSrc(), 0)
        self.assertEqual(call.getDist(), -1)
        self.assertEqual(call.getTime(), 4.37472729)

    def test_algo(self):
        calls = Calls("resources/Calls_a.csv")
        building = Building("resources/B1.json")
        algo = OfflineAlgo(building)
        algo.handleCalls(calls, "output.csv")
        elevator_commands = Calls("output.csv")
        self.assertEqual(len(elevator_commands.calls), 167)



if __name__ == '__main__':
    unittest.main()
