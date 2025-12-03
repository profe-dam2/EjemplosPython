import curses
# Permite controlar la terminal (capturar teclas, redibujar pantalla, ...)

def menu(strscr):
    opciones = ["Opción 1","Opción 2", "Opción 3"]

    while True:
        # Limpiar la pantalla
        strscr.clear()

        # Escribir por pantalla
        strscr.addstr("MENÚ PRINCIPAL")

        for i, opcion in enumerate(opciones):
            strscr.addstr( i+2 , 0, opcion)

        # Espera a que el usuario pulse una tecla
        tecla = strscr.getch()

        if tecla == ord('q'):
            break

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
        curses.nocbreak()
        strscr.keypad(False)
        curses.echo()
        curses.endwin()
