
import random
import os

# Variables
digitos= '0123456789'
numero= ''
muertos=0
heridos=0
intento= None
intentos= []
salir = False


# Presentacion
os.system('clear')

print('______________________________________________')
print()
print('      Juego de Muertos y Heridos              ')
print('  Consiste en adivinar el numero de 4 dígitos ')
print('        Tienes 15 oportunidades               ')
print('       Pulsa Enter para comenzar              ')
print()
print('______________________________________________')

input()

# Gererar un número aleatorio de 4 dígitos
while len(numero)<4:
    digito=random.choice(digitos)
    if digito not in numero:
        numero += digito


# Bucle principal
while True:
    os.system('clear')
    
    print('********************************')
    print('       MUERTOS Y HERIDOS        ')
    print('********************************')
    print('     NUMERO  -   M   -   H      ')
    print('     ------  -   ---------      ')

    # Imprimir intentos 
    for i in range(len(intentos)):
        plantilla = '*     {}   -   {}  -    {}     *'
        print(plantilla.format(intentos[i][0],intentos[i][1],intentos[i][2]))
    
    #  Si gana
    if numero == intento:
        print('*         Has acertado. Has ganado     *')
        print('*Lo has logrado en ', len(intentos), 'intentos *')
        break
    
    # Si pierde por limite de 15 intentos
    if len(intentos) >= 15:
        print('*     Se acabaron los intentos. Has perdido      *')
        print('*        El numero era: ',numero, '*')
        break

    # Condiciones del intento del jugador: salir, 4 digitos, solo numeros, no repetidos
    while True:
        intento = input('=> Introduce un intento ("q" salir):  ')
        if intento == "q":
            salir = True
            break 
        elif len(intento) < 4 or len(intento)>4:
            print('Debe ser solo de 4 digitos')
        elif intento[0] not in digitos or intento[1] not in digitos or \
            intento[2] not in digitos or intento[3] not in digitos:
            print('Solo números del 0 al 9')
        elif intento[0] == intento[1] or intento[0] == intento[2] or intento[0] == intento[3] or \
            intento[1] == intento[2] or intento[1] == intento[3] or intento[2] == intento[3]:
            print('No se pueden repetir numeros')
        else:
            break

    # Salir del bucle principal
    if salir:
        print('El número era ',numero)
        break
    
    # Bucle para agregar los muertos y heridos del intento del jugador
    for i in range(4):
        if intento[i] in numero:
            if intento[i] == numero[i]:
                muertos +=1
            else:
                heridos +=1
    
    intentos.append([intento, muertos, heridos])
    muertos=0
    heridos=0
