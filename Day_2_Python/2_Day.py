import turtle

def draw_rose(num_petals=36, petal_size=100, stem_length=300, petal_color="red", stem_color="green"):
    # Set up the turtle
    turtle.bgcolor("white")
    turtle.speed(10)
    turtle.color(petal_color)

    # Draw the petals
    angle = 360 / num_petals
    for _ in range(num_petals):
        turtle.circle(petal_size, 60)  # Draw a semicircle
        turtle.left(120)                 # Turn left
        turtle.circle(petal_size, 60)  # Draw another semicircle
        turtle.left(120)                 # Turn left to the original position
        turtle.left(angle)               # Rotate to draw the next petal

    # Draw the stem
    turtle.right(90)
    turtle.color(stem_color)
    turtle.pensize(5)
    turtle.forward(stem_length)

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the rose
draw_rose()