import turtle as t
from functionalitati import coordonatele
import time

ecran = t.Screen()
ecran.title('ISS Track')

ecran.bgpic(picname='./map/2489-world-map-design.png')
ecran.cv._rootwindow.resizable(False, False)
satelitul = t.Turtle()
imaginea = './map/ezgif.com-apng-to-gif.gif'
ecran.addshape(imaginea)
satelitul.shape(imaginea)
satelitul.penup()
# ecran.tracer(0)
print(ecran.canvwidth)
print(ecran.canvheight)
while True:
    coordonate: dict = coordonatele()
    x = ((coordonate['x'] * ecran.window_width()) / 360) / 2
    y = ((coordonate['y'] * ecran.window_height()) / 180) / 2
    print(x)
    print(y)
    satelitul.goto(x=x, y=y)
    satelitul.pendown()
    time.sleep(1)
    # ecran.update()

ecran.mainloop()
