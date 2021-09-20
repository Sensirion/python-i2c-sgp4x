import time
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_sgp4x import Sgp40I2cDevice

# Connect to the I²C 1 port /dev/i2c-1
with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
    # Create SGP40 device
    sgp40 = Sgp40I2cDevice(I2cConnection(i2c_transceiver))

    # Measure every second for one minute
    for _ in range(60):
        time.sleep(1)
        sraw_voc = sgp40.measure_raw()
        # use default formatting for printing output:
        print("SRAW VOC: {}".format(sraw_voc))
