import serial  # 导入串口包
import time  # 导入时间包
# reviewed: xy
# date: 2022.9.2
# 不可用
# https://blog.csdn.net/wabil/article/details/120210337


# ser = serial.Serial("COM5", 9600, timeout=1)  # 开启com口，波特率，超时1s
# ser.flushInput()  # 清空缓冲区
#
# def serial_read_and_send():
#     while True:
#         count = ser.inWaiting()  # 获取串口缓冲区数据
#         if count != 0:
#             recv = ser.read(ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
#             ser.write(recv.encode())  # 收到的数据发出去
#             print("[", time.time(), "]recv->", recv)  # 打印一下子
#         time.sleep(0.2)  # 延时0.2秒，免得CPU出问题(线程占满时间片)


def serial_send_and_read(serialport):
    '''
    先发送后接收
    发送：FF 01 02 03 04 05 06 07 08 FE
    '''
    while True:
        send_string = 'FF 01 02 03 04 05 06 07 08 FE/ '
        serialport.write(send_string.encode())  # 发送串口数据
        count = serialport.inWaiting()  # 获取串口缓冲区数据
        print('count:')
        print(count)
        if count != 0:
            recv = serialport.read(serialport.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
            print("[", time.time(), "]recv->", recv)  # 打印一下子
        time.sleep(0.5)  # 延时，免得CPU出问题(线程占满时间片)


if __name__ == '__main__':
    serialport = serial.Serial()
    # 端口号
    serialport.port = 'COM5'
    # 波特率
    serialport.baudrate = 9600
    # 数据位数
    serialport.bytesize = 8
    # 校验位
    serialport.parity = serial.PARITY_NONE
    # 停止位数
    serialport.stopbits = 1
    serialport.timeout = 0.001
    serialport.close()

    if not serialport.is_open:
        serialport.open()
    # serial_read_and_send()
    print("waiting receive uart data...")
    serial_send_and_read(serialport)
