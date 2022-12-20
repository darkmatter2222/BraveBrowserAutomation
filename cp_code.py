import usb_hid
import time
from adafruit_hid.mouse import Mouse


mouse = Mouse(usb_hid.devices)

while True:
    time.sleep(10)

    for i in range(1, 50):
        mouse.move(y=-10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(y=+10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=-10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=+10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=-10)
        mouse.move(y=-10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=+10)
        mouse.move(y=+10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=-10, y=-10)

    time.sleep(1)

    for i in range(1, 50):
        mouse.move(x=+10, y=+10)



