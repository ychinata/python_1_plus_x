import os
import json
# 债券功能
class Debt:
    def __init__(self):
        self.debt_path = "data/debt_info.txt"

    # 添加债券
    def add_Debt(self):
        #识别债券是否存在，默认是False
        debt_status = False
        debt_id = input("请输入债券编号：")
        debt_name = input("请输入债券名称：")
        debt_price = input("请输入债券价格：")
        # 判断是否为空
        if debt_id and debt_name and debt_price:
            debt_data ={"debt_id":debt_id,
                        "debt_name":debt_name,"debt_price":debt_name}
            # 写入在债券，是否存在
            debt_list = self.read_debt()
            # None,0,"",[],(),{a:b}是false
            if debt_list:
                 #数据存在，判断id是否重复
                for debt in debt_list:
                    debt = json.loads(debt)
                    if debt["debt_id"] == debt_id:
                        debt_status = True

                #判断debt_status
                if debt_status:
                    print("债券已存在，不能重复添加...")
                else:
                    with open(self.debt_path, "a", encoding="utf-8") as af:
                        af.write(json.dumps(debt_data, ensure_ascii=False) + "\n")
                    print("债券添加成功...")
            else:
                with open(self.debt_path,"w",encoding="utf-8") as wf:
                    wf.write(json.dumps(debt_data,ensure_ascii=False)+"\n")
                print("债券添加成功...")
        else:
            print("债券信息不能为空，请重新输入...")
   # 读出数据
    def read_debt(self):
       # 判断数据是否存在
       # 判断文件路径是否存在
        if os.path.exists(self.debt_path):
            with open(self.debt_path,"r",encoding="utf-8") as rf:
                debt_list = rf.readlines()
            return debt_list
        else:
            return None

if __name__ == '__main__':
    print("这是debt")