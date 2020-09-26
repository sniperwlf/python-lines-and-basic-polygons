from graphics import *
import time


def BresenhamLine(x1, y1, x2, y2):
    """Basado en Algoritmo de linea de Bresenham"""

    # creacion de objeto ventana
    winX = 600
    winY = 600
    win = GraphWin('Linea de Bresenham', winX, winY)
    win.setBackground(color_rgb(0, 0, 0))

    # calcular la distancia entre los 2 puntos
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # calcular el error para cada punto
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)

    # verificacion de punto inicial y punto final
    if x1 > x2:
        x, y = x2, y2
        xend = x1
    else:
        x, y = x1, y1
        xend = x2

    # ciclo para creacion de linea basada en puntos
    PutPixle(win, x, y)
    while x < xend:
        x = x + 1
        if p < 0:
            p = p + duady
        else:
            y = y - 1 if y1 > y2 else y + 1
            p = p + duadydx

        time.sleep(0.01)
        print(x, y)
        PutPixle(win, x, y)

    win.getMouse()
    win.close()


def PutPixle(win, x, y):
    # colocar pixel en coordenadas x,y dentro de la ventana
    pt = Point(x, y)
    pt.setFill(color_rgb(0, 200, 0))
    pt.draw(win)


def main():
    x1 = int(input("Introducir inicio de X: "))
    y1 = int(input("Introducir inicio Y: "))
    x2 = int(input("Introducir final de X: "))
    y2 = int(input("Introducir final de  Y: "))

    BresenhamLine(x1, y1, x2, y2)


if __name__ == "__main__":
    main()