import csv
from csv import writer

class Calls:
    def __init__(self, csv_path):
        self.calls = []
        csv_file = open(csv_path)
        csv_reader = csv.reader(csv_file)
        index = 0
        for row in csv_reader:
            call = Call(row, index)
            self.calls.append(call)
            index += 1
        csv_file.close()


class Call:
    def __init__(self, row, index):
        self.string = row[0]
        self.time = float(row[1])
        self.src = int(row[2])
        self.dist = int(row[3])
        self.id = index
        self.handle = False

    def getString(self):
        return self.string

    def getTime(self):
        return self.time

    def getSrc(self):
        return self.src

    def getDist(self):
        return self.dist

    def getIdCall(self):
        return self.id

    def wasHandle(self):
        return self.handle

    def setWasHandle(self):
        self.handle = True

    def isGoingUp(self):
        return self.src < self.dist


