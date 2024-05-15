import time
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, \
    SensorBridgeShdlcDevice, SensorBridgeI2cProxy
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_sgp4x import Sgp41I2cDevice

# Connect to the SensorBridge with default settings:
#  - baudrate:      460800
#  - slave address: 0
with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    print("SensorBridge SN: {}".format(bridge.get_serial_number()))

    # Configure SensorBridge port 1 for SGP40
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SGP40 device
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
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

    bridge.switch_supply_off(SensorBridgePort.ONE)
