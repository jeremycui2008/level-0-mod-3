import random
import turtle
from tkinter import simpledialog



# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    bill=turtle.Turtle()
    bill.pensize(10)
    for ix in range (1000):
        for i in range (4):
            bill.forward(150)
            bill.left(90)
        rob= simpledialog.askstring(title='color', prompt='what color you want')
        if rob=='brown':
            bill.pencolor('brown')
        elif rob=='purple':
            bill.pencolor('purple')
        elif rob=='green':
            bill.pencolor('green')
        elif rob=='yellow':
            bill.pencolor('yellow')
        elif rob=='blue':
            bill.pencolor('blue')
        elif rob=='red':
            bill.pencolor('red')
        elif rob=='black':
            bill.pencolor('black')
        else:
            bill.pencolor(get_random_color())

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
