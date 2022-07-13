import serial
import time


def serial_write():
    se = serial.Serial('/dev/ttyTHS1', 9600, timeout=1)
    time.sleep(1)
    se.write('TestNull'.encode())
    se.write(b'Test B')
    se.write('Test GB'.encode("GB2312"))
    print('Write Finish')


def serial_read():
    se = serial.Serial('/dev/ttyTHS1', 9600, timeout=1)
    while True:
        time.sleep(1)
        line = se.readline()
        if line:
            se.write('Get\r\n'.encode())
            print(line)


if __name__ == '__main__':
    print('Start')
    serial_write()
    serial_read()
    print('End')
