import random
import turtle
import time

# Pantalla
s = turtle.Screen()
s.bgcolor("orange")
s.title("Carrera de Tortugas Game")

# Tortugas
t = turtle.Turtle()
t2 =turtle.Turtle()
t.hideturtle()
t2.hideturtle()
t.shape("turtle")
t.color("white", "blue")
t.shapesize(2, 2, 2)
t2.shape("turtle")
t2.color("white", "green")
t2.shapesize(2, 2, 2)


# Posición inicial tortugas
t.penup()
t.goto(300, 100)
t.pendown()
t.circle(50)
t.penup()
t.goto(300, 150)
t.goto(-300, 150)
t.pendown()
t.showturtle()
t2.penup()
t2.goto(300, -200)
t2.pendown()
t2.circle(50)
t2.penup()
t2.goto(300, -150)
t2.goto(-300, -150)
t2.pendown()
t2.showturtle()

# Juego
dadoTurno1= 0 
dadoTurno2 = 0

while dadoTurno1 == dadoTurno2:
    turnoJugador1 = input("Jugador Azul-Tira el dado:(s(si)/n(no))->")
    if turnoJugador1 == "s":
        dadoTurno1 = random.randint(1, 6)
        print("El valor de tu dado es::", dadoTurno1)
        turnoJugador2 = input("Jugador Verde-Tira el dado:(s(si)/n(no))->")
        if turnoJugador2 == "s":
            dadoTurno2 = random.randint(1, 6)
            print("El valor de tu dado es:", dadoTurno2)
        else:
            print("Pues entonces no juegas.")
            exit()
    else:
        print("Pues entonces no juegas.")
        exit()
 

print("EMPIEZA LA PARTIDA!")
if dadoTurno1 > dadoTurno2:
    while t.pos() <= (300, 150) and t2.pos() <= (300, -150):
        jugador1 = input("Jugador azul:¿Quieres tirar el dado?(s(si)/n(no))->")
        if jugador1 == "s":
            dado1 = random.randint(1, 6)
            print("El valor de tu dado es:", dado1)
            t.forward(dado1*50)
            if t.pos() >= (250, 150):
                print("ENHORABUENA!HA GANADO EL JUGADOR AZUL!")
                time.sleep(5)
                exit()
            jugador2 = input("Jugador verde:¿Quieres tirar el dado?(s(si)/n(no))->")
            if jugador2 == "s":
                dado2 = random.randint(1, 6)
                print("El valor de tu dado es:", dado2)
                t2.forward(dado2*50)
                if t2.pos() >= (250, -150):
                    print("ENHORABUENA!HA GANADO EL JUGADOR VERDE!")
                    time.sleep(5)
                    exit()
            else:
                print(">Pues entonces, pierdes tu turno!")
                jugador1 = input("Jugador azul:¿Quieres tirar el dado?(s(si)/n(no))->")
                if jugador1 == "s":
                    dado1 = random.randint(1, 6)
                    print("El valor de tu dado es:", dado1)
                    t.forward(dado1*50)
                    if t.pos() >= (250, 150):
                        print("ENHORABUENA!HA GANADO EL JUGADOR AZUL!")
                        time.sleep(5)
                        exit()
        else:
            print(">Pues entonces, pierdes tu turno!")
            jugador2 = input("Jugador verde:¿Quieres tirar el dado?(s(si)/n(no))->")
            if jugador2 == "s":
                dado2 = random.randint(1, 6)
                print("El valor de tu dado es:", dado2)
                t2.forward(dado2*50)
                if t2.pos() >= (250, -150):
                    print("ENHORABUENA!HA GANADO EL JUGADOR VERDE!")
                    time.sleep(5)
                    exit()
else:
    while t.pos() <= (300, 150) and t2.pos() <= (300, -150):
        jugador2 = input("Jugador verde:¿Quieres tirar el dado?(s(si)/n(no))->")
        if jugador2 == "s":
            dado2 = random.randint(1, 6)
            print("El valor de tu dado es:", dado2)
            t2.forward(dado2*50)
            if t2.pos() >= (250, -150):
                print("ENHORABUENA!HA GANADO EL JUGADOR VERDE!")
                time.sleep(5)
                exit()

            jugador1 = input("Jugador azul:¿Quieres tirar el dado?(s(si)/n(no))->")
            if jugador1 == "s":
                dado1 = random.randint(1, 6)
                print("El valor de tu dado es:", dado1)
                t.forward(dado1*50)
                if t.pos() >= (250, 150):
                    print("ENHORABUENA!HA GANADO EL JUGADOR AZUL!")
                    time.sleep(5)
                    exit()
            else:
                print(">Pues entonces, pierdes tu turno!")
                jugador2 = input("Jugador verde:¿Quieres tirar el dado?(s(si)/n(no))->")
                if jugador2 == "s":
                    dado2 = random.randint(1, 6)
                    print("El valor de tu dado es:", dado2)
                    t2.forward(dado2*50)
                    if t2.pos() >= (250, -150):
                        print("ENHORABUENA!HA GANADO EL JUGADOR VERDE!")
                        time.sleep(5)
                        exit()
        else:
            print(">Pues entonces, pierdes tu turno!")
            jugador1 = input("Jugador azul:¿Quieres tirar el dado?(s(si)/n(no))->")
            if jugador1 == "s":
                dado1 = random.randint(1, 6)
                print("El valor de tu dado es:", dado1)
                t.forward(dado1*50)
                if t.pos() >= (250, 150):
                    print("ENHORABUENA!HA GANADO EL JUGADOR AZUL!")
                    time.sleep(5)
                    exit()

    

turtle.done()