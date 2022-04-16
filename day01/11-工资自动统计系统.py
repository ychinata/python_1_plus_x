# 五险一金，税收
# 养老保险（16%，8%），医疗保险（7.7%，2%），
# 失业保险（0.06%,0%），大病互助(0.6%,0)，生育保险(0.8%,0)，
# 住房公积金(10%,10%)
# 5k以下：0
# 5k-3.6w:3%
# 3.6w-14.4w:10%
# 14.4w-30w:20%
# 30w-42w:25%
# 42w-66w:30%
# 66w-96w:35%
# 96w以上:45%

# 五险一金对基数
base = 4000
# 接受职员信息
def get_staff():
    staff_name = input("请输入职员姓名：")
    staff_wages = input("请输入职员薪资：")
    return staff_name,int(staff_wages)

# 计算五险一金
def setment():
    # 养老保险
    dw_yl = base * 0.16
    gr_yl = base * 0.08
    # 医疗保险
    dw_yb = base * 0.077
    gr_yb = base * 0.02
    # 失业保险
    dw_sy = base * 0.0006
    gr_sy = base * 0
    # 大病互助
    dw_db = base * 0.006
    gr_db = base * 0
    # 生育保险
    dw_syb = base * 0.008
    gr_syb = base * 0
    # 住房公积金
    dw_zf = base * 0.1
    gr_zf = base * 0.1

    # 列表:单位，个人
    dw_list = [dw_yl,dw_yb,dw_sy,dw_db,dw_syb,dw_zf]
    gr_list = [gr_yl,gr_yb,gr_sy,gr_db,gr_syb,gr_zf]
    return dw_list,gr_list

# 结算个人所得税
def tax(wages):
    # 个人应缴纳费用
    tax_count = 0
    # 5k以下：0
    if wages <= 5000:
        tax_count = 0
    # 5k-3.6w:3%
    elif 5000 < wages <= 36000:
        tax_count = (wages-5000) * 0.03
    # 3.6w-14.4w:10%
    elif 36000 < wages <= 144000:
        tax_count = (36000-5000) * 0.03 + (wages-36000) * 0.1
    # 14.4w-30w:20%
    elif 144000 < wages <= 300000:
        tax_count = (36000-5000) * 0.03 + (144000-36000) * 0.1 +(wages-144000) * 0.2
    # 30w-42w:25%
    elif 300000 < wages <= 420000:
        tax_count = (36000-5000) * 0.03 + (144000-36000) * 0.1 +\
                    (300000-144000) * 0.2+(wages-300000) * 0.25
    # 42w-66w:30%
    elif 420000 < wages <= 660000:
        tax_count = (36000-5000) * 0.03 + (144000-36000) * 0.1 +\
                    (300000-144000) * 0.2+(420000-300000) * 0.25+(wages-420000) * 0.3
    # 66w-96w:35%
    elif 660000 < wages <= 960000:
        tax_count = (36000-5000) * 0.03 + (144000-36000) * 0.1 +\
                    (300000-144000) * 0.2+(420000-300000) * 0.25+(660000-420000) * 0.3+\
                    (wages -660000) * 0.35
    # 96w以上:45%
    else:
        tax_count = (36000-5000) * 0.03 + (144000-36000) * 0.1 +\
                    (300000-144000) * 0.2+(420000-300000) * 0.25+(660000-420000) * 0.3+\
                    (960000-660000) * 0.35+(wages-960000) * 0.45

    return tax_count

# 格式化展示
def show_finance(name,wages,dw_list,gr_list,tax_count):
    # 无限一金综合
    dw_sum = 0
    gr_sum = 0
    for i in range(len(dw_list)):
        dw_sum += dw_list[i]
        gr_sum += gr_list[i]
    # # 养老保险（16%，8%），医疗保险（7.7%，2%），
    # # 失业保险（0.06%,0%），大病互助(0.6%,0)，生育保险(0.8%,0)，
    # # 住房公积金(10%,10%)
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}\t+{:^6}+\t{:^6}+\t{:^6}\t+".format("分类","单位费","个人费","综合"))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}\t+{:^8}+\t{:^8}+\t{:^6}\t+".format(name,"",wages,""))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("养老保险",dw_list[0],gr_list[0],dw_list[0]+gr_list[0]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("医疗保险", dw_list[1], gr_list[1], dw_list[1] + gr_list[1]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("失业保险", dw_list[2], gr_list[2], dw_list[2] + gr_list[2]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("大病互助", dw_list[3], gr_list[3], dw_list[3] + gr_list[3]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("生育保险", dw_list[4], gr_list[4], dw_list[4] + gr_list[4]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("住房公积金", dw_list[5], gr_list[5], dw_list[5] + gr_list[5]))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}\t+{:^8}+\t{:^8}+\t{:^6}\t+".format("综合", dw_sum, gr_sum, dw_sum + gr_sum))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("个人所得税", "", tax_count, ""))
    print("+-----------+--------+----------+-----------+")
    print("+{:^8}+{:^8}+\t{:^8}+\t{:^6}\t+".format("实发薪资", "", "", wages-gr_sum-tax_count))
    print("+-----------+--------+----------+-----------+")
# __name__ == '__main__': 本文件运行，会执行下面代码，被导入则不会执行
if __name__ == '__main__':
    name,wages = get_staff()
    dw_list,gr_list = setment()
    tax_count = tax(wages)
    show_finance(name,wages,dw_list,gr_list,tax_count)