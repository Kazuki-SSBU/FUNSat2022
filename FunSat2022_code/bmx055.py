from smbus import SMBus
import time
import math

# I2C
class bmx055:
  ACCL_ADDR = 0x19
  ACCL_R_ADDR = 0x02
  GYRO_ADDR = 0x69
  GYRO_R_ADDR = 0x02
  MAG_ADDR = 0x13
  MAG_R_ADDR = 0x42
  i2c = SMBus(1)
  def __init__(self):
    # acc_data_setup : 加速度の値をセットアップ
    self.i2c.write_byte_data(self.ACCL_ADDR, 0x0F, 0x03)
    self.i2c.write_byte_data(self.ACCL_ADDR, 0x10, 0x08)
    self.i2c.write_byte_data(self.ACCL_ADDR, 0x11, 0x00)
    time.sleep(0.5)
  
  def acc_value(self):
    data = [0, 0, 0, 0, 0, 0]
    acc_data = [0.0, 0.0, 0.0]
    try:
        for i in range(6):
            data[i] = self.i2c.read_byte_data(self.ACCL_ADDR, self.ACCL_R_ADDR + i)
        for i in range(3):
            acc_data[i] = ((data[2*i + 1] * 256) + int(data[2*i] & 0xF0)) / 16
            if acc_data[i] > 2047:
                acc_data[i] -= 4096
            acc_data[i] *= 0.0098
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    return acc_data

if __name__ == "__main__":
    bmx = bmx055()
    time.sleep(0.1)

    while True:
        acc = bmx.acc_value()
        print("Accl -> x:{}, y:{}, z: {}".format(acc[0], acc[1], acc[2]))
        print("\n")
        time.sleep(0.1)