# Python - Toy robot task

This folder contains two Python files:
  1. robot.py - Simulation of a robot movement on a table top.
  2. robot_test.py - Testing of robot.py simulation.
  
## Problem
 
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units. . There are no other obstructions on the table surface. . The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.
Create an application that can read in commands of the following form:

PLACE X,Y,F MOVE LEFT RIGHT REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. . The origin (0,0) can be considered to be the SOUTH WEST most corner. . The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed. . MOVE will move the toy robot one unit forward in the direction it is currently facing. . LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. . REPORT will announce the X,Y and orientation of the robot. . A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. . Provide test data to exercise the application.

### Constraints:

The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.

### Example

Input and Output:

  1. PLACE 0,0,NORTH MOVE REPORT Output: 0,1,NORTH
  2. PLACE 0,0,NORTH LEFT REPORT Output: 0,0,WEST
  3. PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT Output: 3,3,NORTH

### Deliverables:
The source files, the test data and any test code.

## Description of solution

Deriving from the problem, two classes are:
  1. Tabletop
  2. Robot
  
### Tabletop

Class *Tabletop* represents the table top on which the robot can move.

It is defined with fixed 5x5 size in __init__():

```bash
def __init__(self, width = 5, height = 5):
        """Initalizes a square tabletop with pre-set width and height."""
        self.width = width
        self.height = height
```
*Tabletop* has one local variable, ordered dictionary *movement* which keys are NORTH, EAST, SOUTH and WEST in that particular order. Ordered dictionary was used because it returns list of keys always in order they were created. Values of *movement* are (x, y) pairs with their corresponding values of increment for x and y axes.

```bash
 movement= OrderedDict([
        ("NORTH",{'x':0,'y':1}),
        ("EAST",{'x':1,'y':0}),
        ("SOUTH",{'x':0,'y':-1}),
        ("WEST",{'x':-1,'y':0})
    ])
```
To use ordered dictionary, one must first import module OrderedDict from collections collection with:

```bash
from collections import OrderedDict
```
*Tabletop* also has one method *isPositionOnTable(x,y)* which returns True if the (x,y) coordinates are in bounds of the table top, and returns False if they are not.

```bash
def isPositionOnTable(x, y):
        """Returns True if pos is in the bounds of tabletop"""
        if x <= 5 and x >-1 and y <= 5 and y>-1:
            return True
        else:
            return False
```

### Robot

Class *Robot* represents the robot moving on the table top. At all times the robot has a particular position and direction (x, y, p) on the table top.

It is defined with __init__(). *posx* is x position, *posy* is y position, *direction* is direction, *output* is what the Robot reports as his final position.
```bash
    def __init__(self, x=0, y=0, p='NORTH'):
        """Initializes a Robot with the given position and direction on the tabletop."""
        self.posx=x
        self.posy=y
        self.direction=p
        self.output=""
```

*Robot* has one local variable, dictionary commands. The keys are all valid commands robot understands, with values that are names of the attributes of *Robot* that are called when the corresponding key commands is issued.

```bash
commands = {'PLACE':'PLACE','MOVE':'MOVE','LEFT':'LEFT','RIGHT':'RIGHT','REPORT':'REPORT','NORTH':'NORTH','EAST':'EAST','SOUTH':'SOUTH','WEST':'WEST'}
```
In order to execute commands, method *executeCommands(commands_string)* must be called and receive one argument which is string of commands for the robot.

*executeCommands* will catch errors when the argument is not string, or does not contain command "PLACE".
Corresponding string will be printed.



```bash
    def executeCommands(self, cmd_string):
        """Follows the given list of commands."""
        try:
            cmd=cmd_string.upper().replace(","," ").split()
            try:
                if "PLACE" in cmd:
                    (...)
                else:
                    raise ValueError
            except ValueError:
                print("Robot can't start moving without PLACE command")
        except TypeError:
            print("Invalid entry - the robot doesn't know what to do.\nTell him with a string of commands.")

```

If there is a "PLACE" command, the application will try to cut off the commands string until it gets to "PLACE" command, because it is supposed to ignore all commands before a valid "PLACE" command.

```bash
try:
    x=cmd.index("PLACE")
    cmd=cmd[x:]
    cmd_it=iter(cmd)
    
    for el in cmd_it:
        if el == "PLACE":
           try:
               getattr(self, el)(int(next(cmd_it)),int(next(cmd_it)))
           except:
               continue
         elif el == "REPORT":
                getattr(self,el)()
                return (self.output)
         elif el in self.commands:
                getattr(self,el)()
         else:
             continue
except:
     """ Silently ignore """
```

Then, it will try to call the attribute "PLACE" and store robots position:

```bash
def PLACE(self,x,y):
        """Sets position and direction of the robot."""
        if Tabletop.isPositionOnTable(x, y):
            self.posx=x
            self.posy=y
```

If the "PLACE" command is not valid, it will continue itteration of commands.
If the command is "REPORT" application stops and returns *output* and itteration stops:

```bash
def REPORT(self):
        """Returns robot position and direction."""
        self.output=str(self.posx)+str(self.posy)+str(self.direction)
     
    
(...)
getattr(self,el)()
return (self.output)
(...)
```

If the command is not valid, itteration continues, and if the command is in *commands* then the corresponding function is called.
