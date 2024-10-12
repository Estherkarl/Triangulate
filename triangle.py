import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
triangle_turtle = turtle.Turtle()
triangle_turtle.shape("turtle")
triangle_turtle.color("blue")
triangle_turtle.speed(1)

# Function to draw an equilateral triangle
def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Move turtle to starting position
triangle_turtle.penup()
triangle_turtle.goto(-50, -50)  # Adjust starting position as needed
triangle_turtle.pendown()

# Draw an equilateral triangle
triangle_size = 100
draw_triangle(triangle_turtle, triangle_size)

# Hide turtle and display result
triangle_turtle.hideturtle()
turtle.done()
