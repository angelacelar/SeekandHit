from collections import OrderedDict

class Tabletop(object):
    """Represents tabletop on wich the robot can move."""

    movement= OrderedDict([
        ("NORTH",{'x':0,'y':1}),
        ("EAST",{'x':1,'y':0}),
        ("SOUTH",{'x':0,'y':-1}),
        ("WEST",{'x':-1,'y':0})
    ])
    
    def __init__(self, width = 5, height = 5):
        """Initalizes a square tabletop with pre-set width and height."""
        self.width = width
        self.height = height

    def isPositionOnTable(x, y):
        """Returns True if pos is in the bounds of tabletop"""
        if x <= 5 and x >-1 and y <= 5 and y>-1:
            return True
        else:
            return False

    



class Robot(object):
    """Represents the robot moving on the tabletop. At all times the robot has
    a particular position and direction (x, y, f) on the tabletop."""
    
    commands = {'PLACE':'PLACE','MOVE':'MOVE','LEFT':'LEFT','RIGHT':'RIGHT','REPORT':'REPORT','NORTH':'NORTH','EAST':'EAST','SOUTH':'SOUTH','WEST':'WEST'}
    
    def __init__(self, x=0, y=0, p='NORTH'):
        """Initializes a Robot with the given position and direction on the tabletop."""
        self.posx=x
        self.posy=y
        self.direction=p
        self.output=""

    def REPORT(self):
        """Returns robot position and direction."""
        self.output=str(self.posx)+str(self.posy)+str(self.direction)

    def PLACE(self,x,y):
        """Sets position and direction of the robot."""
        if Tabletop.isPositionOnTable(x, y):
            self.posx=x
            self.posy=y

    def MOVE(self):
        """Simulates a single time-step."""
        temp=Tabletop.movement[self.direction]
        tempx=self.posx+temp['x']
        tempy=self.posy+temp['y']

        self.PLACE(tempx,tempy)
        
        

    def LEFT(self):
        """Rotates robot to the left."""
        if self.direction == "NORTH":
            self.direction="WEST"
        else:
            a=list(Tabletop.movement.keys())
            ind=a.index(self.direction)-1
            self.direction=a[ind]


    def RIGHT(self):
        """Rotates robot to the right."""
        if self.direction == "WEST":
            self.direction="NORTH"
        else:
            a=list(Tabletop.movement.keys())
            ind=a.index(self.direction)+1
            self.direction=a[ind]

    def NORTH(self):
        self.direction = "NORTH"

    def EAST(self):
        self.direction = "EAST"

    def SOUTH(self):
        self.direction = "SOUTH"

    def WEST(self):
        self.direction = "WEST"
    
    def executeCommands(self, cmd_string):
        """Follows the given list of commands."""
        try:
            cmd=cmd_string.upper().replace(","," ").split()
            try:
                if "PLACE" in cmd:
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
                        """Silently ignore"""
                else:
                    raise ValueError
            except ValueError:
                print("Robot can't start moving without PLACE command")
        except TypeError:
            print("Invalid entry - the robot doesn't know what to do.\nTell him with a string of commands.")

