import time
from blinkstick import blinkstick


def _data_set(red=0, green=0, blue=255):
    data = [green, red, blue]
    for i in range(0, 31):
        data.extend([green, red, blue])
    return data


def turn_all_on(red=0, green=0, blue=255):
    led = blinkstick.find_first()
    led.set_led_data(0, _data_set(red, green, blue))


def turn_all_off():
    led = blinkstick.find_first()
    led.set_led_data(0, _data_set(0, 0, 0))


def turn_on_sequence(red=0, green=0, blue=255, step=0.1):
    try:
        turn_all_off()
        led = blinkstick.find_first()
        for i in range(1, 32):
            led.set_color(0, i, green, red, blue)
            time.sleep(step)

    except KeyboardInterrupt:
        print("Exiting... Bye!")
        turn_all_off()


def turn_off_sequence(red=0, green=0, blue=255, step=0.1):
    try:
        turn_all_on(red, green, blue)
        led = blinkstick.find_first()
        for i in range(32, -1, -1):
            led.set_color(channel=0, index=i, red=0, green=0, blue=0)
            time.sleep(step)

    except KeyboardInterrupt:
        print("Exiting... Bye!")
        turn_all_off()


def blink_all(red=0, green=0, blue=255, repeats=99, freq=0.1):
    try:
        for i in range(repeats):
            turn_all_on(red, green, blue)
            time.sleep(freq)
            turn_all_off()
            time.sleep(freq)

    except KeyboardInterrupt:
        print("Exiting... Bye!")
        turn_all_off()
        

# turn_all_off()
# turn_on_sequence('red')
# time.sleep(2)

# turn_all_off()
# turn_off_sequence(255, 255,0)

blink_all(0, 120, 0, 10, 0.2)

