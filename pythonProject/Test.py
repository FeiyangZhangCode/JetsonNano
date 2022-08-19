import time
import datetime
import INA219


file_address = './TestData/'
loop_num = 0
i_last = 0.0
file_rec = open(file_address + 'UPS.txt', 'a')
str_time = datetime.datetime.now().strftime('%H:%M:%S.%f')
ina_mess, i_value = INA219.get_ina219_data()
i_last = i_value
# print(str_time, str(loop_num), ina_mess)
file_rec.write(str_time + '   ' + str(loop_num) + '\n' + ina_mess)

while True:
    time.sleep(1)
    loop_num += 1
    # if loop_num % 2 == 0:
    str_time = datetime.datetime.now().strftime('%H:%M:%S.%f')
    ina_mess, i_value = INA219.get_ina219_data()
    print(str_time, ina_mess)
    file_rec.write(str_time + '   ' + '\n' + ina_mess)
    if (i_last - i_value) > 1.0:
        # os.system('shutdown now')
        print('shutdown', i_last)
        i_last = i_value
    else:
        i_last = i_value