
class ElevatorsCommands:
    def __init__(self, building):
        self.commands = []
        self.building = building
        for i in range(building.getNumberOfElevetor()):
            self.commands.append([])

    def addCommandToElevator(self, command):
        self.commands[command.elevator].append(command)

    def writeOutput(self, path):
        f = open(path, "w")
        for elevator_commands in self.commands:
            for command in elevator_commands:
                f.write(command.getRow() +"\n")
        f.close()

    def getIdleElevator(self, time):
        return [elevator for elevator in range(len(self.commands)) if
                self.getElevatorFinishTimeForAllCommand(elevator) <= time]

    def getElevatorPosition(self, time, elevator):
        if time >= self.getElevatorFinishTimeForAllCommand(elevator):
            if len(self.commands[elevator]) == 0:
                return 0
            return self.commands[elevator][-1].getDst()
        elev_commands = self.commands[elevator]
        building_elevator = self.building.getElevator(elevator)
        for command in elev_commands:
            if time <= command.getTime() and building_elevator.calcTime(command.getSrc(), command.getDst(), 0) <= time:
                for floor in range(command.getSrc + 1, command.getDst()):
                    if building_elevator.calcTime(command.getSrc(), floor, 0) > time:
                        return floor - 1

    def getElevatorFinishTimeForAllCommand(self, elevator):
        if len(self.commands[elevator]) == 0:
            return 0
        elevatorCommand = self.commands[elevator][-1]
        time = elevatorCommand.time
        return time + self.building.getElevator(elevator).calcTime(elevatorCommand.getSrc(), elevatorCommand.getDst(),
                                                                   0)


class ElevatorCommand:
    def __init__(self, src, dst, time, elevator):
        self.src = src
        self.dst = dst
        self.time = time
        self.elevator = elevator

    def getTime(self):
        return self.time

    def getSrc(self):
        return self.src

    def getDst(self):
        return self.dst

    def getRow(self):
        return "Elevator call,{},{},{},{},{}".format(self.time, self.src, self.dst, -2, self.elevator)
