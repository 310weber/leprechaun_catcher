# ST VL6180X ToF range finder setup for shell - copy and past into shell
# - power explorer board with 3.3 V
# - explorer board includes pull-ups on i2c

"""
After fixing following points, anything was working perfectly (several million
bidirectional transfers without any error) :
Adding "baudrate=75000" to the linux i2c_bcm2708 driver (default is 100000).
For doing this you have to create a "/etc/modprobe.d/i2c.conf" file and adding a
"options i2c_bcm2708 baudrate=75000" line.
"""

import Adafruit_I2C
from time import sleep

bus = smbus.SMBus(1)
address = 0x29


def write(location, value):
    bus.write_byte_data(address, location, value)
    return -1


def read(location):
    read_data = bus.read_byte_data(address, location)
    return read_data


def read_range(j=0):
    while (read(0x4d) & 0x01) == 0:
        j += 1
        if j > 3:
            print "Not ready to range."
            return -1
        sleep(0.01)
    print "Ready to range. %s" % bin(read(0x4d))
    write(0x18, 0x01)
    j = 0
    while ((read(0x4f) >> 2) & 0x01) == 0:
        j += 1
        if j > 3:
            print "Measurement not complete. %s %d" % (
                bin(read(0x4d) >> 4), read(0x62))
            return -1
        sleep(0.05)
    range_read = read(0x62)
    write(0x15, 0x07)
    print"Ranging complete: %d" % range_read
    return range_read