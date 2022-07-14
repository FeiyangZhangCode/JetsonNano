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
    se1 = serial.Serial('/dev/ttyTHS2', 9600, timeout=1)
    print('Read Ready')
    while True:
        time.sleep(1)
        line = se1.readline()
        if line:
            se1.write('Get\r\n'.encode())
            print(line)


if __name__ == '__main__':
    print('Start')
    # serial_write()
    serial_read()
    print('End')
