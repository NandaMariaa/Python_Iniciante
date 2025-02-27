import turtle as mod_turtle

turtle = mod_turtle.Turtle()     # Turtle turtle = new Turtle() no java
window = mod_turtle.Screen()

window.title("turtle and ye game")

# tipagem dinamica é coisa de jamelão
speed: float = 16
angular_speed: float = 45
penactive: bool = True

def kup():
    turtle.forward(speed)

def kright():
    turtle.right(angular_speed)

def kleft():
    turtle.left(angular_speed)

def kdown():
    turtle.back(speed)

def kspace():
    global penactive #  dizer para o satã que é o processador do python que queremos usar a variavel que eu declarei e nn uma copia dela >:(

    if penactive == True:
        turtle.penup()
    else:
        turtle.pendown()

    penactive = not penactive

mod_turtle.onkey(kup, "Up")
mod_turtle.onkey(kright, "Right")
mod_turtle.onkey(kdown, "Down")
mod_turtle.onkey(kleft, "Left")
mod_turtle.onkey(kspace, "space")

mod_turtle.listen()
mod_turtle.mainloop()
