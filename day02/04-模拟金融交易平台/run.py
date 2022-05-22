from debt import Debt
# 运行功能
def show():
    print("""
        ******************
        *   0->退出系统    *
        *   1->添加债券    *
        *   2->查询债券    *
        *   3->添加用户    *
        *   4->查看用户    *
        *   5->充值金额    *
        *   6->买入债券    *
        ******************
    """)

def run():
    while True:
        show()
        res = input("请输入操作命令:")
        if res:
            if res == "0":
                print("系统已退出....")
                break
            elif res == "1":
                # 添加
                Debt().add_Debt()
        else:
            print("输入不能为空,请重新输入...")

if __name__ == '__main__':
    run()

# 122055 10中铁G4 104.45
# 122071 11航海02 51.00