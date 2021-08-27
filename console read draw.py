import turtle as a
import sys

t = a.Turtle()

def draw(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)

sides = 5

if(len(sys.argv) > 1):
    if(sys.argv[1].isdigit()):
      if (isinstance(int(sys.argv[1]), int)) and (int(sys.argv[1]) < 10):
        print("Drawing with sides " + sys.argv[1])
        draw(int(sys.argv[1]))
else:
    draw(int(sides))

a.Screen().exitonclick()
