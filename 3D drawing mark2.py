import turtle

side = int(input("Enter the length of the side of square: "))

a = turtle.Turtle()

def draw(n, base, height, angle_one, angle_two):
  for x in range(n):
    # Draw base
    a.forward(base)
    a.left(angle_one)

    # Draw h1
    a.forward(height)
    a.left(angle_two)

def drawraw(n, base, height, angle_one):
  angle_two = 180 - angle_one

  draw(n, base, height, angle_one, angle_two)

  draw(n, base, base, 90, 90)

  a.forward(base)
  a.left(angle_one)
  a.forward(height)
  a.left(90 - angle_one)

  draw(n, base, base, 90, 90)

  
  # Move
  a.forward(base)
  a.left(90)

  # Draw part 3 (last part)
  draw(2, base, height, angle_one, angle_two)


def cube(side, angle = 60):
  drawraw(2, 2*side, side, angle)

a.backward(100)
a.color("red")
a.fillcolor("red")
a.begin_fill()
cube(side)
a.end_fill()

a.penup()
a.backward(100)
a.pendown()
a.color("green")
a.fillcolor("green")
a.begin_fill()
cube(side)
a.end_fill()

a.penup()
a.forward(100)
a.pendown()
a.color("blue")
a.fillcolor("blue")
a.begin_fill()
cube(side)
a.end_fill()

turtle.Screen().exitonclick()