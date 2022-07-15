import serial
import time


def serial_write():
    se = serial.Serial('/dev/ttyTHS1', 9600, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

    time.sleep(1)
    str_b = 'fF-1.0'
    # print(len(str_b))
    se.write(str_b.encode())
    print(str_b)
    str_c = 'fR123.50'
    se.write(str_c.encode('UTF-8'))
    print(str_c)
    # line = se.readline().strip()
    # if line:
    #     # se.write('Get\r\n'.encode())
    #     str_c = str(line)
    #     print(str_c)
        # print(len(str_c))




def serial_read():
    se = serial.Serial('/dev/ttyTHS1', 9600, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    while True:
        time.sleep(1)
        line = se.readline()
        if line:
            se.write('Get'.encode())
            se.write(line)
            print(line)



print('Start')
serial_write()
serial_read()
print('End')
