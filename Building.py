import json

from Elevator import Elevator


class Building:
    def __init__(self, building_path):
        f = open(building_path, )
        data = json.load(f)
        f.close()
        self.min_floor = data["_minFloor"]
        self.max_floor = data["_maxFloor"]
        self.elevator = []
        for elevat in data['_elevators']:
            self.elevator.append(Elevator(elevat))

    def getMinFloor(self):
        return self.min_floor

    def getMaxFloor(self):
        return self.max_floor

    def getElevator(self, elevator):
        return self.elevator[elevator]

    def getNumberOfElevetor(self):
        return len(self.elevator)

    def getDistance(self):
        return abs(self.getMaxFloor()-self.getMinFloor())
