# opp_task1
 
 Name: tal ornan    i.d:209349356
 
 Name : Amit Huri   i.d:323919399
 
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
    
### The results:

##### Case a:

building|the results
--- | --- |
B1|Total waiting time: 5796.0,  average waiting time per call: 34.706586826347305,  unCompleted calls,0,  certificate, -231884611
B2|Total waiting time: 25968.0,  average waiting time per call: 151.859649122807,  unCompleted calls,14,  certificate, -339305094

##### Case b:

building|the results
--- | --- |
B3|2188566.8571428587,  average waiting time per call: 1150.6660657954042,  unCompleted calls,116,  certificate, -3888000867
B4|Total waiting time: 2514140.0,  average waiting time per call: 1308.0853277835588,  unCompleted calls,153,  certificate, -4400675104
B5|Total waiting time: 274520.0,  average waiting time per call: 142.16468151216986,  unCompleted calls,31,  certificate, -370608452

##### Case c:

building|the results
--- | --- |
B3|Total waiting time: 7075192.999999943,  average waiting time per call: 3675.4249350649056,  unCompleted calls,406,  certificate, -12752329667
B4|Total waiting time: 2237791.0,  average waiting time per call: 1184.643197458973,  unCompleted calls,163,  certificate, -4176834365
B5|Total waiting time: 71149.0,  average waiting time per call: 37.486301369863014,  unCompleted calls,0,  certificate, -212891900

##### Case d:

building|the results
--- | --- |
B3|Total waiting time: 1543838.5714285753,  average waiting time per call: 812.9744978560165,  unCompleted calls,83,  certificate, -2885910037
B4|Total waiting time: 3524421.0,  average waiting time per call: 1855.9352290679305,  unCompleted calls,368,  certificate, -6235063532
B5|Total waiting time: 69427.0,  average waiting time per call: 36.8117709437964,  unCompleted calls,0,  certificate, -205859433


### UML Diagram:
![image](https://user-images.githubusercontent.com/76403961/142656669-93232128-7287-4b34-a17a-00503cca8817.png)











    
    
