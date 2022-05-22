import os
import json
from datetime import datetime
class Account:
    def __init__(self):
        self.account_path = "data/account_info.txt"
    # 添加用户
    def add_account(self):
        # 身份id，用户名，金额，债券编号，债券名称，债券数量，创建时间
        account_id = input("请输入身份id：")
        account_name = input("请输入用户名：")

        if account_id and account_name:
            account = {"account_id":account_id,"account_name":account_name,
                       "capital":0,"debt_id":"","debt_name":"",
                       "debt_count":"","create_time":self.get_time()}
            # 读出信息
            account_list = self.read_account()
            if account_list:
                print("用户已存在，不能重复创建...")
            else:
                with open(self.account_path,"w",encoding="utf-8") as wf:
                    wf.write(json.dumps(account,ensure_ascii=False)+"\n")
        else:
            print("用户信息不能为空...")

    # 读出用户信息
    def read_account(self):
        if os.path.exists(self.account_path):
            with open(self.account_path,"r",encoding="utf-8") as rf:
                account_list = rf.readlines()
                return account_list
        else:
            return None

    # 获取本地时间
    def get_time(self):
        timer = datetime.now()
        return "{}/{}/{} {}:{}:{}".format(timer.year,timer.month,
                            timer.day,timer.hour,timer.minute,timer.second)

    # 查询用户
    def find_account(self):
        account_list = self.read_account()
        if account_list:
            self.show_account(account_list)
        else:
            print("用户不存在，请先添加...")

    # 显示用户
    def show_account(self,account_list):
        # 身份id，用户名，金额，债券编号，债券名称，债券数量，创建时间
        print("-"*94)
        print("{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^20}\t".format(
            "身份id","用户名","金额","债券编号","债券名称","债券数量","创建时间",
        ))
        print("-"*94)
        for account in account_list:
            account = json.loads(account)
            print("{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:>20}\t".format(
                account["account_id"], account["account_name"], account["capital"],
                account["debt_id"], account["debt_name"], account["debt_count"],
                account["create_time"]
            ))
            print("-" * 94)

    # 充值
    def recharge(self):
        account_list = self.read_account()
        if account_list:
            account = json.loads(account_list[0])
            count = input("请输入充值金额：")
            capital = float(account["capital"]) + float(count)
            account["capital"] = capital
            account["create_time"] = self.get_time()
            with open(self.account_path,"a",encoding="utf-8") as af:
                af.write(json.dumps(account,ensure_ascii=False)+"\n")
            # 改成一致
            self.update_capital(capital)
            print("充值已完成...")
        else:
            print("还未添加用户，请先添加...")

    # 将多有金额的金额改成一致
    def update_capital(self,capital):
        with open(self.account_path,"r",encoding="utf-8") as rf:
            account_list = rf.readlines()
        with open(self.account_path,"w",encoding="utf-8") as wf:
            for account in account_list:
                account = json.loads(account)
                account["capital"] = capital
                wf.write(json.dumps(account,ensure_ascii=False)+"\n")
if __name__ == '__main__':
    a = Account()
    print(a.get_time())