import turtle
# todo : here
new_turtle=turtle.Turtle();
new_turtle.speed(10)
def square():
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)

def square1():
    new_turtle.left(135)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)
    new_turtle.right(60)
    new_turtle.forward(100)

#square()
#new_turtle.forward(200)
#square()

#abc = "sad";
#while abc == "sad":
 #   new_turtle.right(90)
for i in range(1):
    square()
for i in range(50):
    square1()

turtle.done()