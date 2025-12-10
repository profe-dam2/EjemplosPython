import curses
import json
from pathlib import Path

# Permite controlar la terminal (capturar teclas, redibujar pantalla, ...)

import requests

def opcion1():
    # Limpiar la pantalla
    terminal.clear()
    # Escribir por pantalla
    terminal.addstr(0,0,"HAS ELEGIDO UNA OPCION 1")
    terminal.addstr(1,0,"Pulsa una tecla para volver a menu")
    # Esto es una pausa
    curses.nocbreak()
    curses.echo()
    mensaje = terminal.getch()

    curses.cbreak()
    datos = {"mensaje":mensaje}

    #Enviar mensaje a discord
    requests.post("http://192.168.23.5:5678/webhook/mensaje",json=datos)

    terminal.getch()

def opcion2():
    # Limpiar la pantalla
    terminal.clear()
    # Escribir por pantalla
    terminal.addstr(0,0,"HAS ELEGIDO UNA OPCION 2")
    terminal.addstr(1,0,"Pulsa una tecla para volver a menu")
    # Esto es una pausa
    terminal.getch()

def opcion3():
    # Limpiar la pantalla
    terminal.clear()
    # Escribir por pantalla
    terminal.addstr(0, 0, "HAS ELEGIDO UNA OPCION 3")
    terminal.addstr(1, 0, "Pulsa una tecla para volver a menu")
    # Esto es una pausa
    terminal.getch()

def listar():
    ruta = Path.cwd() / "tienda"
    seleccion = 0
    while True:
        terminal.clear()
        terminal.addstr(0, 0, "HAS ELEGIDO LISTAR")
        elementos = [ruta.parent] + sorted(ruta.iterdir())
        for i, elemento in enumerate(elementos):
            nombre = elemento.name
            if elemento == ruta.parent:
                nombre = "Volver"
            if seleccion == i:
                terminal.addstr(i + 2, 0, nombre, curses.A_REVERSE)
            else:
                terminal.addstr(i + 2, 0, nombre)

        tecla = terminal.getch()
        if tecla == curses.KEY_DOWN and seleccion < len(elementos) - 1:
            seleccion += 1
        elif tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == ord('\n'):
            ruta = elementos[seleccion]
            seleccion = 0


def menu(terminal):
    opciones = ["Opción 1","Opción 2", "Opción 3","Listar", "Salir"]
    seleccion = 0
    while True:
        # Limpiar la pantalla
        terminal.clear()

        # Escribir por pantalla
        terminal.addstr("MENÚ PRINCIPAL")

        # Pintar las opciones en la terminal
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                terminal.addstr(i+2,0, opcion, curses.A_REVERSE)
            else:
                terminal.addstr( i+2,0,opcion)

        # Espera a que el usuario pulse una tecla
        tecla = terminal.getch()

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
            elif seleccion == 3:
                listar()
            elif seleccion == 4:
                pass


if __name__ == '__main__':
    print("inicio")

    # Inicializa curses y obtiene la pantalla (terminal)
    terminal = curses.initscr()

    # Activar detección de teclas especiales (flechas, enter, etc)
    terminal.keypad(True)

    # Desactiva el eco del teclado
    # Las teclas pulsadas no se muestran
    curses.noecho()

    # Activar modo lectura inmediata de teclas (no espera Enter)
    curses.cbreak()

    # Oculta el cursor
    curses.curs_set(0)

    try:
        menu(terminal)
    finally:
        # Libera los recursos de la termianl
        curses.nocbreak()
        terminal.keypad(False)
        curses.echo()
        curses.endwin()
