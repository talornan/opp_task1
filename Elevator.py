import json
from Calls import Calls


class Elevator:
    def __init__(self, elevator_dic):
        self.id = elevator_dic["_id"]
        self.speed = elevator_dic["_speed"]
        self.minFloor = elevator_dic['_minFloor']
        self.maxFloor = elevator_dic['_maxFloor']
        self.closeTime = elevator_dic['_closeTime']
        self.openTime = elevator_dic['_openTime']
        self.startTime = elevator_dic['_startTime']
        self.stopTime = elevator_dic['_stopTime']
        self.currPosition = 0

    def getId(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getMinFloor(self):
        return self.minFloor

    def getMaxFloor(self):
        return self.maxFloor

    def getCloseTime(self):
        return self.closeTime

    def getOpenTime(self):
        return self.openTime

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime

    def getPosition(self):
        return self.currPosition

    def calcTime(self, src, dst, stops):
        if src == dst:
            return 0
        floors_time = abs(src - dst) / self.getSpeed()
        elevator_time = self.openTime + self.closeTime + self.stopTime + self.startTime
        return (floors_time + elevator_time*(stops + 1))
