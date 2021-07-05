from turtle import *
import random
import os

########
# Vars #
########
turtle_arr = []
scoreboard = []
WIDTH, HEIGHT = 500, 500
SPEED = 10
MOVEMENT_RANGE = 5

###########
# Classes #
###########
class TurtleRacer:
    def __init__(self, color, initPos, position):
        #Vars
        self.turtle = Turtle(shape="turtle")
        self.color = color
        self.initPos = initPos
        self.position = position

        #Init turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setpos(-(WIDTH//2), self.initPos)
        self.turtle.pendown()
        self.turtle.speed(SPEED)

    # Get x coord
    def get_turtle_x(self):
        return int(self.turtle.pos()[0])

    # Move turtle forward a random number of pixels
    def move(self):
        self.turtle.forward(random.randrange(0, MOVEMENT_RANGE))

    # Get turtle position in the race (the top left one is the 1st, below is the 2nd...)
    def get_position(self):
        return self.position
    
    # Move the turtle to the edge of the screen if surpassed and draw a dot
    def win_animation(self):
        self.turtle.setpos(WIDTH // 2, self.turtle.pos()[1])
        self.turtle.dot(50, self.color)

#############
# Functions #
#############
# Generate random hex color
def random_hex_color():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))

# Calculate spacing between turtles in y coord
def set_init_pos(total, pos):
    value = (HEIGHT // total * pos - 200)
    return(value)

# Clear console and setup screen
def init_screen():
    os.system("cls")
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle race by alesbe")

    print("""
    =========================
    = Turtle race by alesbe =
    =========================

    """)

# Create turtles (the count var and reversed method is for assigning the turtle position)
def init_turtles():
    count = 1
    for i in reversed(range(num_turtles)):
        turtle = TurtleRacer(random_hex_color(), set_init_pos(num_turtles, i), count)
        turtle_arr.append(turtle)
        count+=1

# Format and print scoreboard
def show_scoreboard():
    print("")
    for i in scoreboard:
        print(f"The turtle number {i} is, {scoreboard.index(i) + 1}º!")

########
# Main #
########
init_screen()

# Number of turtles input and initialize
num_turtles = int(numinput("Turtle race", "Number of turtles (1-10): ", 5, minval=1, maxval= 10));
init_turtles()

input("Press enter on console to start!")

# Main loop
while True:
    if not turtle_arr: #if all the turtles has won (if turtle_arr is empty)
        break

    # Pick a random turtle and move it
    t = random.choice(turtle_arr)
    t.move()

    # Check if the turtle won
    if t.get_turtle_x() >= WIDTH//2:
        t.win_animation()
        scoreboard.append(t.get_position())
        turtle_arr.pop(turtle_arr.index(t))

# End the program
show_scoreboard()
done()