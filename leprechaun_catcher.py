# Servo Control
import RPi.GPIO as GPIO
from ST_VL6180X import VL6180X
from time import sleep


"""-- subroutines --"""
def set_pwm(pwm_property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + pwm_property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + pwm_property + " value: " + value)


def set_servo(angle):
    set_pwm("servo", str(angle))


def check_distance():
    return tof_sensor.get_distance()


def check_light():
    return tof_sensor.get_ambient_light(20)


"""-- variables and setup --"""
switch_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

tof_address = 0x29
tof_sensor = VL6180X(address=tof_address, debug=debug)
tof_sensor.get_identification()
if tof_sensor.idModel != 0xB4:
    print"Not a valid sensor id: %X" % tof_sensor.idModel
else:
    print"Sensor model: %X" % tof_sensor.idModel
    print"Sensor model rev.: %d.%d" % \
         (tof_sensor.idModelRevMajor, tof_sensor.idModelRevMinor)
    print"Sensor module rev.: %d.%d" % \
         (tof_sensor.idModuleRevMajor, tof_sensor.idModuleRevMinor)
    print"Sensor date/time: %X/%X" % (tof_sensor.idDate, tof_sensor.idTime)
tof_sensor.default_settings()

set_pwm("delayed", "0")
set_pwm("mode", "servo")
set_pwm("servo_max", "195")
set_pwm("active", "1")

delay_period = 0.1
arm_up = 98             # angle of arm in 'up' position
arm_down = 12           # angle of arm in 'down' position
trap_active = None      # flag if trap is active or not

while True:
    # check activation switch - up is True (active), down is False (deactivated)
    if GPIO.input(switch_pin) is False and trap_active is not False:
        set_servo(arm_up)
        trap_active = False
        print"Trap deactivated. Safe for maintenance."
    elif GPIO.input(switch_pin) is True and trap_active is not True:
        set_servo(arm_up)
        trap_active = True
        print "Trap activated.  Approach with caution."

    # if the trap is active, check for Leprechauns
    if trap_active is True:
        distance = check_distance()
        light = check_light()
        if distance in range(60, 90):
            set_servo(arm_down)
            if light < 100:
                print"You have caught a Leprechaun.  He's not very bright."
            else:
                print"You have caught an exceptionally bright Leprechaun!"
        else:
            set_servo(arm_up)

    sleep(0.2)