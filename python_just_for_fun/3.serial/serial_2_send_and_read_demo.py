import binascii
from serial import Serial
# reviewed: xy
# date: 2022.9.2
# 参考https://blog.csdn.net/aggie4628/article/details/123150250
# 可用!!!


def serial_send_and_read_once():
    '''  发送并读取串口:一次  '''
    hexCmd = "FF 01 02 03 04 05 06 07 08 FE"
    hexCmd = hexCmd.replace(' ', '')  # 去除空格
    cmd = binascii.a2b_hex(hexCmd)  # 转换为16进制串

    # 4. Hex发送
    write_len = com.write(cmd)
    print("write:")
    print(cmd)

    # 5.读取
    rels = com.read_all()
    print(rels)
    while True:
        rels = com.read_all()
        if rels:  # 返回不为空 跳出死循环
            break
    if rels:
        print("read:")
        print(rels)


def serial_send_and_read_loop():
    # TODO 循环
    '''  发送并读取串口:循环  '''
    hexCmd = "FF 01 02 03 04 05 06 07 08 FE"
    hexCmd = hexCmd.replace(' ', '')  # 去除空格
    cmd = binascii.a2b_hex(hexCmd)  # 转换为16进制串

    # 4. Hex发送
    write_len = com.write(cmd)
    print("write:")
    print(cmd)

    # 5.读取
    rels = com.read_all()
    print(rels)
    while True:
        rels = com.read_all()
        if rels:  # 返回不为空 跳出死循环
            break
    if rels:
        print("read:")
        print(rels)


if __name__ == "__main__":
    # 1.实例化串口及各项参数
    com = Serial(port='COM5', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                 dsrdtr=False, rtscts=False, xonxoff=False, timeout=2)

    # 2.查看串口状态 如果串口没打开打开它
    if com.isOpen() == False:
        com.open()

    # 3. 如果串口已打开 关了重开
    if com.isOpen() == True:
        com.close()
        com.open()

        # begin
        # 主体串口动作函数
        serial_send_and_read_once()
        # end

    # 结束:关闭串口
    if com.isOpen() == True:
        com.close()

