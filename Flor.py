import math
import turtle
# Configuración inicial de la ventana
turtle.bgcolor("white")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)
# Dibuja la espiral del girasol
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        # Dibuja la hoja con la estructura deseada
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()
# Dibuja el tallo
turtle.penup()
turtle.goto(0, -300)  # Posición del tallo más abajo
turtle.pendown()
turtle.color("green")
turtle.pensize(10)
turtle.setheading(90)  # Apuntar hacia arriba
turtle.forward(200)   # Dibuja el tallo
# Dibuja la hoja
turtle.penup()
turtle.goto(40, -290)  # Posición de la hoja más abajo
turtle.pendown()
turtle.begin_fill()
turtle.setheading(60)  # Orientación de la hoja
for _ in range(3):
    turtle.forward(70)
    turtle.left(120)  # Cambio de dirección para formar la hoja
turtle.end_fill()
# Agrega un mensaje
turtle.penup()
turtle.goto(0, 280)
turtle.color("red")
turtle.write("Para mi Alisson te Quiero eres la mejor ❤️ ...", align="center", font=("Arial", 24, "bold"))
# Oculta la tortuga y muestra el resultado
turtle.hideturtle()
turtle.done()

