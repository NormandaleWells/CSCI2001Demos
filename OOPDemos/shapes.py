
import turtle

class Rectangle:
        def __init__(self, x, y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.color = "black"

        def draw(self, t):
                t.penup()
                t.goto(self.x, self.y)
                t.pendown()
                t.color(self.color)
                t.setheading(0)
                t.forward(self.width)
                t.left(90)
                t.forward(self.height)
                t.left(90)
                t.forward(self.width)
                t.left(90)
                t.forward(self.height)

def main():
        win = turtle.Screen()
        t = turtle.Turtle()
        r = Rectangle(10, 10, 40, 30)
        r.draw(t)
        win.exitonclick()

if __name__ == "__main__":
        main()
