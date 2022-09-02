import serial  # pip install pyserial
import time

# reviewed: hx
# date: 2022.8.31

# 参考代码：https://blog.csdn.net/weixin_46096498/article/details/119645804
serialport = serial.Serial()


# 配置串口参数（与单片机的配置保持一致）
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
# time.sleep(0.05)  # 时间设置参考串口传输速率
# num = serialport.inWaiting()
# if num > 0:
#     data = serialport.read(num)
#     print(data)


every_time = time.strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
data = ''
while True:
    data = serialport.readline()
    print(every_time, data)



# TODO 串口读取数据
# 2.单片机周期发消息
