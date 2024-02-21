import turtle

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("white")
# set title of screen
screen.title("USA Flag")

# Create a turtle object
usa_flag = turtle.Turtle()
# set the cursor/turtle speed
usa_flag.speed(0)
usa_flag.penup()
usa_flag.hideturtle()

# Flag dimensions
flag_height = 250
flag_width = 475

# Starting point
start_x = -237
start_y = 125

# Stripe dimensions
stripe_height = flag_height / 13
stripe_width = flag_width

# Star dimensions
star_size = 10

# Function to draw a filled rectangle
def draw_fill_rectangle(x, y, height, width, color):
   usa_flag.goto(x, y)
   usa_flag.pendown()
   usa_flag.color(color)
   usa_flag.begin_fill()
   for _ in range(2):
       usa_flag.forward(width)
       usa_flag.right(90)
       usa_flag.forward(height)
       usa_flag.right(90)
   usa_flag.end_fill()
   usa_flag.penup()

# Function to draw a star
def draw_star(x, y, color, length):
   usa_flag.goto(x, y)
   usa_flag.setheading(0)
   usa_flag.pendown()
   usa_flag.begin_fill()
   usa_flag.color(color)
   for _ in range(5):
       usa_flag.forward(length)
       usa_flag.right(144)
   usa_flag.end_fill()
   usa_flag.penup()

# Function to draw 13 stripes
def draw_stripes():
   x = start_x
   y = start_y
   for stripe in range(13):
       color = "red" if stripe % 2 == 0 else "white"
       draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
       y -= stripe_height




# Function to draw the blue square
def draw_square():
   square_height = (7/13) * flag_height
   square_width = (0.76) * flag_height
   draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


# Function to draw stars
def draw_stars(rows, stars_per_row):
   gap_between_stars = 30
   gap_between_lines = stripe_height + 6
   y = 112 if rows == 6 else 100
   for row in range(rows):
       x = -222 if rows == 6 else -206
       for _ in range(stars_per_row):
           draw_star(x, y, 'white', star_size)
           x += gap_between_stars
       y -= gap_between_lines

# Draw the flag
draw_stripes()
draw_square()
draw_stars(6, 6)
draw_stars(5, 5)

# Hide the cursor/turtle
usa_flag.hideturtle()
# Keep the screen open until manually closed
screen.mainloop()