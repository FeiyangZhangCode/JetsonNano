import cv2
import datetime


# 返回摄像头格式
def get_camera_data(cap, cap_num):
    str_Info = 'C' + str(cap_num) + ':' + str(cap.get(3)) + '*' + str(cap.get(4)) + '; FPS' + str(cap.get(5)) + '\n'
    str_fourcc = str("".join([chr((int(cap.get(cv2.CAP_PROP_FOURCC)) >> 8 * i) & 0xFF) for i in range(4)])) + '\n'
    str_Info = str_Info + str_fourcc
    return str_Info


# 开始主程序
int_ca0 = 0
int_ca1 = 1

# 第一个摄像头0
cap0 = cv2.VideoCapture(int_ca0)
cap0.set(6, 1196444237)
cap0.set(3, 1920)
cap0.set(4, 1080)
cap0.set(5, 30)
fps0 = cap0.get(cv2.CAP_PROP_FPS)
size0 = (int(cap0.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap0.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 保存视频
# out0 = cv2.VideoWriter('TestData/camera_0.avi', fourcc, fps0, size0)

# 第二个摄像头1q
cap1 = cv2.VideoCapture(int_ca1)
cap1.set(6, 1196444237)
cap1.set(3, 1920)
cap1.set(4, 1080)
cap1.set(5, 30)
fps1 = cap1.get(cv2.CAP_PROP_FPS)
size1 = (int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# out1 = cv2.VideoWriter('TestData/camera_1.avi', fourcc, fps1, size1)

# 打开文件夹
str_fileAddress = './TestData/'
# 读取时间作为文件名，开始本轮采集
str_Time = datetime.datetime.now().strftime('%H-%M-%S')
file_rec = open(str_fileAddress + str_Time + '.txt', 'w', encoding='utf-8')
file_rec.write(get_camera_data(cap0, int_ca0))
file_rec.write(get_camera_data(cap1, int_ca1))
# 设置循环计数器，每循环多少帧进行一次操作
loop_num = 0
while True:

    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    loop_num = loop_num + 1
    # if loop_num % fps0 == 0:
    # 读取时间
    str_Time = datetime.datetime.now().strftime('%H-%M-%S-%f')
    # 记录数据
    file_rec.write(str_Time + '  ' + str(loop_num) + '\n')
    print(str_Time + '  ' + str(loop_num))
    # 保存图片
    cv2.imwrite(str_fileAddress + "P0-" + str_Time + '.jpg', frame0)
    cv2.imwrite(str_fileAddress + "P1-" + str_Time + '.jpg', frame1)
    # cv2.putText(frame, str_putText,
    #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # cv2.imshow('frame0', frame0)
    # cv2.imshow('frame1', frame1)

    # out0.write(frame0)
    # out1.write(frame1)

    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

file_rec.close()
cap0.release()
# out0.release()
cap1.release()
# out1.release()
cv2.destroyAllWindows()
