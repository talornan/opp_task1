import json
import offlineAlgo
from Elevator import Elevator
import csv
from Building import Building
from Calls import Calls
from Calls import Call
from offlineAlgo import OfflineAlgo

import sys


if __name__ == '__main__':
    building_path = sys.argv[1]
    csv_path = sys.argv[2]
    output = sys.argv[3]
    f = open(building_path, )
    data = json.load(f)
    building = Building(building_path)
    calls = Calls(csv_path)
    algo = OfflineAlgo(building)
    algo.handleCalls(calls, output)

