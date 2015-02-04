# Servo Control
import time
import RPi.GPIO as GPIO

switch_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + property + " value: " + value)


def set_servo(angle):
    set("servo", str(angle))


set("delayed", "0")
set("mode", "servo")
set("servo_max", "195")
set("active", "1")
delay_period = 0.1

while True:
    # for angle in range(0, 180):
    #     setServo(angle)
    #     time.sleep(delay_period)
    # for angle in range(0, 180):
    #     setServo(180 - angle)
    #     time.sleep(delay_period)

    if GPIO.input(switch_pin) is False:
        set_servo(12)
        print"12 degrees"
    else:
        set_servo(98)
        print "98 degrees"
    time.sleep(1)
