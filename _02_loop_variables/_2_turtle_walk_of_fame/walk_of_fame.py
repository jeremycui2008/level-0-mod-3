import turtle

if __name__ == '__main__':
    bill = turtle.Turtle()
    bill.shape('turtle')
    bill.color('blue', 'green')
    bill.speed(0)
    bill.penup()
    # TODO 1) Set the X position of the turtle so that it starts on the left.
    bill.goto(-400,0)
    bill.pendown()
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    x=-450
    for y in range(1000000000):
        for i in range(6):
            bill.right(144)
            bill.forward(30)
        bill.penup()
        bill.goto(x,0)
        x=x-50
        bill.right(216)
        bill.pendown()

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.


# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
