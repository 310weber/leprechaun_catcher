# ST VL6180X ToF range finder program
# - power explorer board with 3.3 V
# - explorer board includes pull-ups on i2c

import smbus
from time import sleep
import RPi.GPIO as GPIO  # Import GPIO functions
import sys

# setup i2c bus and ToF address
bus = smbus.SMBus(1)
address = 0x29

# Set output pin numbers for LEDS
GPIO.setmode(GPIO.BCM)  # Use GPIO numbering scheme (not pin numbers)
LED = [17, 27]  # List of GPIOs to use for LED output

# Setup GPIOs and initial states
for i in range(len(LED)):
    GPIO.setup(LED[i], GPIO.OUT)  # Set all as output
    print("GPIO_%d is output" % LED[i])
    GPIO.output(LED[i], 0)  # Turn all LEDs off


# i2c write function
def write(location, value):
    bus.write_byte_data(address, location, value)
    return -1


# i2c read function
def read(location):
    read_data = bus.read_byte_data(address, location)
    return read_data


# Range finding function
def read_range(j=0):
    while (read(0x4d) & 0x01) == 0:
        j += 1
        if j > 3:
            print "Not ready to range."
            return -1
        sleep(0.01)
    write(0x18, 0x01)
    j = 0
    while (read(0x4f) & 0x04) == 0:
        j += 1
        if j > 3:
            print "Measurement not complete. %d" % read(0x4d)
            return -1
        sleep(0.01)    range1 = read(2)
    range_read = read(0x62)
    write(0x15, 0x07)
    print"Ranging complete: %d" % range_read
    return range_read


# LED lighting function
def led_out(value):
    for i in range(len(LED)):
        GPIO.output(LED[i], value & (1 << i))  # Set LEDs based on value


"""-- MAIN LOOP --"""
while True:
#    write(0, 0x51)  # Set SRF to return distance in cm
#    sleep(0.1)
#    # while range() == 0xFF:        # Wait for range finder to be ready
#    # pass                          # Do nothing
#    rng = (read_range() + read_range()) / 2

#    print "\rDistance is: %3.0f" % rng,
#    sys.stdout.flush()  # Flush output buffer to force print update

    # Set LED output based on range value
#    if rng >= 50:
#        led_out(0x01)
#    elif rng >= 40:
#        led_out(0x03)
#    elif rng >= 30:
#        led_out(0x07)
#    elif rng >= 20:
#        led_out(0x0F)
#    elif rng >= 10:
#        led_out(0x1F)
#    else:
#        led_out(0x3F)

read_range()
sleep(2)