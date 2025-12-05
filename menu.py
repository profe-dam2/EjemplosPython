import curses
import json

# Permite controlar la terminal (capturar teclas, redibujar pantalla, ...)

import requests

def opcion1():
    # Limpiar la pantalla
    strscr.clear()
    # Escribir por pantalla
    strscr.addstr(0,0,"HAS ELEGIDO UNA OPCION 1")
    strscr.addstr(1,0,"Pulsa una tecla para volver a menu")
    # Esto es una pausa
    curses.nocbreak()
    curses.echo()
    mensaje = strscr.getch()

    curses.cbreak()
    datos = {"mensaje":mensaje}

    #Enviar mensaje a discord
    requests.post("http://192.168.23.5:5678/webhook/mensaje",json=datos)

    strscr.getch()

def opcion2():
    # Limpiar la pantalla
    strscr.clear()
    # Escribir por pantalla
    strscr.addstr(0,0,"HAS ELEGIDO UNA OPCION 2")
    strscr.addstr(1,0,"Pulsa una tecla para volver a menu")
    # Esto es una pausa
    strscr.getch()

def opcion3():
    # Limpiar la pantalla
    strscr.clear()
    # Escribir por pantalla
    strscr.addstr(0, 0, "HAS ELEGIDO UNA OPCION 3")
    strscr.addstr(1, 0, "Pulsa una tecla para volver a menu")
    # Esto es una pausa
    strscr.getch()



def menu(strscr):
    opciones = ["Opción 1","Opción 2", "Opción 3"]
    seleccion = 0
    while True:
        # Limpiar la pantalla
        strscr.clear()

        # Escribir por pantalla
        strscr.addstr("MENÚ PRINCIPAL")

        # Pintar las opciones en la terminal
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                strscr.addstr(i+2,0, opcion, curses.A_REVERSE)
            else:
                strscr.addstr( i+2,0,opcion)

        # Espera a que el usuario pulse una tecla
        tecla = strscr.getch()

        if tecla == ord('q'):
            break
        elif tecla == curses.KEY_DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == ord('\n'): # ENTRA AQUI SI HAS PULSADO LA TECLA ENTER

            # Si la seleccion es 0, he elegido la primera opción
            if seleccion == 0:
                opcion1()
            elif seleccion == 1:
                opcion2()
            elif seleccion == 2:
                opcion3()


if __name__ == '__main__':
    print("inicio")

    # Inicializa curses y obtiene la pantalla (terminal)
    strscr = curses.initscr()

    # Activar detección de teclas especiales (flechas, enter, etc)
    strscr.keypad(True)

    # Desactiva el eco del teclado
    # Las teclas pulsadas no se muestran
    curses.noecho()

    # Activar modo lectura inmediata de teclas (no espera Enter)
    curses.cbreak()

    # Oculta el cursor
    curses.curs_set(0)

    try:
        menu(strscr)
    finally:
        # Libera los recursos de la termianl
        curses.nocbreak()
        strscr.keypad(False)
        curses.echo()
        curses.endwin()
