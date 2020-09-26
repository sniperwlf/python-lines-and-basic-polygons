from graphics import *
from random import randint


def main():
    win = GraphWin("Polygono", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    # Prompt the User for 3 mouse clicks
    message = Text(Point(0, 8), "Click en puntos para crear polygono")
    message.draw(win)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    # Store coordinates in variables x1, x2 etc
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    point4 = win.getMouse()
    point5 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    x3 = point3.getX()
    y3 = point3.getY()
    x4 = point4.getX()
    y4 = point4.getY()
    x5 = point5.getX()
    y5 = point5.getY()

    # dibujar polygono
    polygono = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4), Point(x5, y5))
    polygono.setFill(color_rgb(r, g, b))
    polygono.setOutline("red")
    polygono.setWidth(4)

    polygono.draw(win)

    win.getMouse()
    win.close()

main()
