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


def tirar(tirada):
    tirada = sorted(tirada)
    input('presiona ENTER para tirar los dados')
    print(tirada)
    print(" 1  2  3  4  5")
    return tirada


def elegir_reroll(tirada):
    reroll = map(int, input("ingrese los numeros de los dados que quiere volver a tirar\n").strip().split())
    for dado in reroll:
        tirada[dado - 1] = rnd.randint(1, 6)
    return tirada

def tachar(eleccion):
    return grilla.append(str(elecciones[eleccion]) + ': 0')

def sumar(eleccion):
    return grilla.append(str(elecciones[eleccion]) + ': ' + str(puntos[eleccion]))

def check(eleccion):
    if eleccion == 'g':
        return es_generala(tirada)
    elif eleccion == 'p':
        return es_poker(tirada)
    elif eleccion == 'f':
        return es_full(tirada)
    elif eleccion == 'e':
        return es_escalera(tirada)
    else:
        return True

def elegir(eleccion):
    opcion = input('Elegi gd: Generala Doble g: Generala, p: Poker, f: Full, e: Escalera, 1: Unos, 2: Dos, 3: Tres, 4: Cuatros, 5: Cincos, 6: Seis\n')
    validar = check(opcion)
    if eleccion == 't':
        tachar(opcion)
        return print(grilla)
    elif eleccion == 'a' and validar == True:
         sumar(opcion)
         return print(grilla)
    elif eleccion =='a' and validar == False:
        tachar(opcion)
        return print(grilla)
    else:
        return print('Te haz equivocado')


grilla = []

tirada = []

while len(grilla) <= 10:
    for i in range(1, 6):
        tirada.append(rnd.randint(1, 6))


    tirada = tirar(tirada)

    for i in range(0,2):
        tirada = elegir_reroll(tirada)
        tirada = tirar(tirada)

    puntos = {}
    puntos['gd'] = 60
    puntos['g'] = 50
    puntos['p'] = 45
    puntos['f'] = 35
    puntos['e'] = 25
    puntos['6'] = tirada.count(6) * 6
    puntos['5'] = tirada.count(5) * 5
    puntos['4'] = tirada.count(4) * 4
    puntos['3'] = tirada.count(3) * 3
    puntos['2'] = tirada.count(2) * 2
    puntos['1'] = tirada.count(1) * 1

    elecciones = {}
    elecciones['1'] = 'Unos'
    elecciones['2'] = 'Dos'
    elecciones['3'] = 'Tres'
    elecciones['4'] = 'Cuatros'
    elecciones['5'] = 'Cincos'
    elecciones['6'] = 'Seis'
    elecciones['e'] = 'Escalera'
    elecciones['f'] = 'Full'
    elecciones['p'] = 'Poker'
    elecciones['g'] = 'Generala'
    elecciones['gd'] = 'Generala Doble'

    while True:
        eleccion = input('t: tachar, a: agregar\n')
        if eleccion == 'a' or eleccion == 't':
            break

    primera = elegir(eleccion)

    tirada.clear()


