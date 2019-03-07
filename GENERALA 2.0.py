import random as rnd


def es_generala(tirada):  # dice si una tirada ORDENADA es una generala
    return tirada[0] == tirada[4]


def es_poker(tirada):  # dice si una tirada ORDENADA es un poker
    return tirada.count(tirada[0]) == 4 or tirada.count(tirada[4]) == 4


def es_full(tirada):  # dice si una tirada ORDENADA es un full
    return (tirada.count(tirada[0]) == 3 and tirada.count(tirada[4]) == 2) or (
                tirada.count(tirada[0]) == 2 and tirada.count(tirada[4]) == 3)


def es_escalera(tirada):  # dice si una tirada ORDENADA es una escalera
    return tirada == [1, 2, 3, 4, 5] or tirada == [2, 3, 4, 5, 6] or tirada == [3, 4, 5, 6, 1]

def sin_juego(tirada): #dice si una tirada ORDENADA no tiene juego
    return tirada != es_escalera(tirada) and tirada != es_full(tirada) and tirada != es_generala(tirada) \
           and tirada != es_poker(tirada)

def tirar(tirada):
    tirada = sorted(tirada)
    input('presiona ENTER para tirar los dados')
    print(tirada)
    print("1 2 3 4 5")
    return tirada


def elegir_reroll(tirada):
    reroll = map(int, input("ingrese los numeros de los dados que quiere volver a tirar\n").strip().split())
    for dado in reroll:
        tirada[dado - 1] = rnd.randint(1, 6)
    return tirada

puntos = []
tirada = []
for i in range(1, 6):
    tirada.append(rnd.randint(1, 6))

jugador_1 = input('Escribir el nombre del jugador 1\n')

jugador_2 = input('Escribir el nombre del jugador 2\n')

jugador_3 = input('Escribir el nombre del jugador 3\n')

jugador_4 = input('Escribir el nombre del jugador 4\n')

tirada = tirar(tirada)

for i in range(0,2):
    tirada = elegir_reroll(tirada)
    tirada = tirar(tirada)

if es_generala(tirada):
    puntos + 50
    print("salio generala")

if es_full(tirada):
    puntos + 20
    print("salio full")

if es_poker(tirada):
    puntos + 35
    print("salio poker")

if es_escalera(tirada):
    puntos + 25
    print("salio escalera")

if sin_juego(tirada):
    print('YOU LOOSE')