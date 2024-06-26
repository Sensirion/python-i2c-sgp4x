import time
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_sgp4x import Sgp41I2cDevice

# Connect to the I²C 1 port /dev/i2c-1
with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
    # Create SGP41 device
    sgp41 = Sgp41I2cDevice(I2cConnection(i2c_transceiver))

    print("SGP41 Serial Number: {}".format(sgp41.get_serial_number()))

    # Run conditioning for 10 seconds
    # WARNING: To avoid damage to the sensing material the conditioning must not exceed 10s!
    for _ in range(10):
        time.sleep(1)
        sraw_voc = sgp41.conditioning()
        # use default formatting for printing output:
        print("SRAW VOC: {}\t\tSRAW NOx: conditioning".format(sraw_voc))

    # Measure every second for one minute
    for _ in range(60):
        time.sleep(1)
        sraw_voc, sraw_nox = sgp41.measure_raw()
        # use default formatting for printing output:
        print("SRAW VOC: {}\t\tSRAW NOx: {}".format(sraw_voc, sraw_nox))
