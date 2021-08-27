import turtle

a = turtle.Turtle()

# Calculations

def draw(n, base, height, angle_one, angle_two):
  for x in range(n):
      # Draw base
    a.forward(base)
    a.left(angle_one)

    # Draw h1
    a.forward(height)
    a.left(angle_two)

# Draw part 1
draw(2, 100, 50, 60, 120)
draw(2, 100, 100, 90, 90)

# Move cursor
a.forward(100)
a.left(60)
a.forward(50)
a.left(30)

# Draw part 2
draw(2, 100, 100, 90, 90)

# Move
a.forward(100)
a.left(90)

# Draw part 3 (last part)
draw(2, 100, 50, 60, 120)


turtle.Screen().exitonclick()