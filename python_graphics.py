import turtle as a
import sys


def draw(n):
  print("Drawing a polygon with sides ", n)

  t = a.Turtle()
  for i in range(n):
    t.forward(100)
    t.left(360/n)

sides = int(input("Enter number of sides: "))
if sides < 11 and sides > 1:
  draw(sides)
else:
  draw(3)

a.Screen().exitonclick()
