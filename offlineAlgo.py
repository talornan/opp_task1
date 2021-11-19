import ElevatorsCommand


class OfflineAlgo:
    def __init__(self, building):
        self.building = building
        self.elevatorsCommands = ElevatorsCommand.ElevatorsCommands(building)

    def calcCommandFromCalls(self, elevatorCurrentPos, time, calls, isGoingUp, elevator):
        if len(calls) == 0:
            return
        floors = [call.getSrc() for call in calls] + [call.getDist() for call in calls]
        floors.sort(reverse=isGoingUp)
        prevFloor = elevatorCurrentPos
        currTime = time
        for floor in floors:
            if prevFloor != floor:
                command = ElevatorsCommand.ElevatorCommand(prevFloor, floor, currTime, elevator)
                self.elevatorsCommands.addCommandToElevator(command)
                currTime += self.building.getElevator(elevator).calcTime(prevFloor, floor, 0)

    def getAllCallsForElevatorWithOutExceedDestOmer(self, src, dst, start_time, calls, elevator):
        isGoingUp = dst > src
        same_direction = [curr_call for curr_call in calls if curr_call.isGoingUp() == isGoingUp]
        src_position = [curr_call for curr_call in same_direction if
                        (isGoingUp and src <= curr_call.getSrc() <= dst) or (
                                    not isGoingUp and dst <= curr_call.getSrc() < src)]
        positions = [curr_call for curr_call in src_position if (isGoingUp and src <= curr_call.getDist() <= dst) or (
                    not isGoingUp and dst >= curr_call.getDist() >= src)]

        number_of_stops = 0
        handle_calls = []
        for curr_call in positions:
            if self.building.getElevator(elevator).calcTime(src, start_time, number_of_stops) <= curr_call.getTime():
                number_of_stops += 1
                handle_calls.append(curr_call)
                curr_call.setWasHandle();
        return handle_calls

    def getAllCallsForElevatorOmer(self, src, dst, start_time, calls, elevator):
        isGoingUp = dst > src
        same_direction = [curr_call for curr_call in calls if curr_call.isGoingUp() == isGoingUp]
        src_position = [curr_call for curr_call in same_direction if
                        (isGoingUp and src <= curr_call.getSrc() <= dst) or (
                                    not isGoingUp and dst <= curr_call.getSrc() < src)]
        number_of_stops = 0
        handle_calls = []
        for curr_call in src_position:
            if self.building.getElevator(elevator).calcTime(src, curr_call.getDist(),
                                                            number_of_stops) >= curr_call.getTime():
                number_of_stops += 1
                handle_calls.append(curr_call)
                curr_call.setWasHandle();
        return handle_calls

    def getAllCallsForElevator(self, elevator, call, calls):
        call.setWasHandle()

        time = self.elevatorsCommands.getElevatorFinishTimeForAllCommand(elevator)
        elevator_position = self.elevatorsCommands.getElevatorPosition(time, elevator)
        time += self.building.getElevator(elevator).calcTime(elevator_position, call.getSrc(), 0)
        handle_calls = self.getAllCallsForElevatorOmer(call.src, call.getDist(), time, calls, elevator)
        if len(handle_calls) == 0:
            self.calcCommandFromCalls(elevator_position, time, [call], call.getDist() > call.getSrc(), elevator)
        else:
            max_dest = max([curr_call.getDist() for curr_call in handle_calls])
            dest_time = self.building.getElevator(elevator).calcTime(call.getSrc(), call.getDist(), len(handle_calls))
            beni = self.getAllCallsForElevatorWithOutExceedDestOmer(call.getDist(), max_dest, dest_time, calls,
                                                                    elevator)
            self.calcCommandFromCalls(elevator_position, time, handle_calls + beni, call.getDist() > call.getSrc(),
                                      elevator)

    def getBestElevatorForCall(self, call):
        time = call.getTime()
        idle_elevators = self.elevatorsCommands.getIdleElevator(time)
        if len(idle_elevators) > 0:
            # get elevator that is the closet to the call source position
            closetElevator = idle_elevators[0]
            for elevator in idle_elevators:
                if abs(self.elevatorsCommands.getElevatorPosition(time, elevator) - call.getSrc()) < abs(
                        self.elevatorsCommands.getElevatorPosition(time, closetElevator) - call.getSrc()):
                    closetElevator = elevator
            return elevator
        # return elevator handle the least amount of commands,
        # maybe we should add also some calculation for the how long it takes completing those commands
        min_elevator = 0;
        prevCommandLen = len(self.elevatorsCommands.commands[0])
        for elevator in range(len(self.elevatorsCommands.commands)):
            if len(self.elevatorsCommands.commands[elevator]) < prevCommandLen:
                min_elevator = elevator
                prevCommandLen = len(self.elevatorsCommands.commands[elevator])
        return min_elevator

    def offlineOptimizer(self, calls, index):
        if len(calls) <= 1:
            return calls;
        if calls[index].getSrc() == calls[index + 1].getSrc() and calls[index].getDist() == calls[index + 1].getDist():
            if abs(calls[calls[index].getSrc()] - calls[index +1].getDist()) > 40 and  calls[index +1].getTime() - calls[index].getTime() < 230:
                return calls[1:], True
        elif calls[index].isGoingUp() and calls[index + 1].isGoingUp() and calls[index].getSrc() == calls[index +1].getSrc() and calls[index + 1].getTime() - calls[index].getTime() < 230:
            if abs(calls[index + 1].getDist() - calls[index].getDist()) < 10:
                if(calls[0].getDist() < calls[index + 1].getDist()):
                    calls[0].time = calls[index + 1].getTime()
                    calls[index + 1].time += 10
                    calls[index + 1].src = calls[0].getDist()
                    return calls, True
        return calls, False

    def handleCalls(self, calls, output):
        calls = calls.calls
        optimizerIndex = 0
        calls, wasOpt = self.offlineOptimizer(calls, optimizerIndex)
        while(optimizerIndex  < len(calls) -1):
            if wasOpt:
                calls, wasOpt = self.offlineOptimizer(calls, optimizerIndex)
            else:
                optimizerIndex += 1;

        while len(calls) > 0:
            elevator = self.getBestElevatorForCall(calls[0])
            self.getAllCallsForElevator(elevator, calls[0], calls[1:])
            calls = [call for call in calls if not call.wasHandle()]
        self.elevatorsCommands.writeOutput(output)
