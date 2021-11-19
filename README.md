# opp_task1

### Literature review :
1.https://stackoverflow.com/a/493350

2.https://www.i-programmer.info/programmer-puzzles/203-sharpen-your-coding-skills/4561-sharpen-your-coding-skills-elevator-puzzle.html?start=1

3.https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/

4.https://stackoverflow.com/questions/12009556/datastructure-for-elevator-mechanism/35373696#35373696

### The algorithm:
Solution :
In order to solve this assignment I've decided to create the following object
Building - building is an object with min_floor & max_floor as a field, and a list of Elevator object. this object created by parsing the json bulding. each field have a getter 

##### method

Elevator - this object contains field related to elevator - speed, close/open times and stops time. each field have a getter method
Call - this object present a single row from the calls.csv field. I've created field for src,dst,time & string object.
ElevatorCommand - present command for the elevator, what is the next floor the elevator should go
ElevatorCommands - container for multiple commands. this class also contains method that helps to calcualte the current position of the elevator
Ex1 - simple main that running the algo

##### Offline algo:

in case thee are two calls that are with the same direcition, and the src & value are very closed, and the number of distanct floor between them is high,
we will do both calls within the same elevator calls, even if we will have to waite for the second calls
First step - choose the best elevator for the first call, trying to choose elevator that is idle & the closet to the current position.
    if all the elevator are already assign, we will waite for the first elevator that will be idle/
    Second steps - choose all the calls that are on the same direction of the first call, the src in within the floor range, and that a stop if the floor will not add much time
    execute those calls.
    execute again the first step, after filteting all the task that already completed
    
### The solutions:

    
    
