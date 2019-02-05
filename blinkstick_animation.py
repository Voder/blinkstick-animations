import time
from blinkstick import blinkstick


# data_all_green = [255,0,0]
# data_all_red = [0,255,0]
# data_all_blue = [0, 0, 255]

# for i in range(0, 31):
#     data_all_green.extend([255, 0, 0])
#     data_all_red.extend([0,255, 0])
#     data_all_blue.extend([0, 0, 255])

def turnAllOff():
    for led in blinkstick.find_all():
        for i in range(1, 32):
            led.set_color(channel=0, index=i, red=0, green=0, blue=0)


def turnOnSequence(color='blue', step=0.1):
    try:
        turnAllOff()
        for led in blinkstick.find_all():
            for i in range(1, 32):
                led.set_color(channel=0, index=i, name=color)
                time.sleep(step)

    except KeyboardInterrupt:
        print("Exiting... Bye!")
        turnAllOff()


turnOnSequence('red')
time.sleep(5)
turnAllOff()