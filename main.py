import turtle as t
from functionalitati import coordonatele
import time

ecran = t.Screen()
ecran.title('ISS Track')

ecran.bgpic(picname='./map/81937-blue-world-globe-map-free-hq-image.png')
ecran.cv._rootwindow.resizable(False, False)
satelitul = t.Turtle()
imaginea = './map/ezgif.com-apng-to-gif.gif'
ecran.addshape(imaginea)
satelitul.shape(imaginea)
ecran.tracer(0)
satelitul.hideturtle()
satelitul.penup()
print(ecran.window_height())
print(ecran.window_width())
while True:
    coordonate: dict = coordonatele()
    x = (coordonate['x'] * ecran.window_width()) / 360 / 2
    y = (coordonate['y'] * ecran.window_height()) / 180 / 2
    satelitul.goto(x=round(number=x, ndigits=2), y=round(number=y, ndigits=2))
    satelitul.showturtle()
    satelitul.pendown()
    print(x)
    print(y)
    time.sleep(5)
    ecran.update()


