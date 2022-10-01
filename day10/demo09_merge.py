import pandas as pd
# reviewed:2022.9.30

left = pd.DataFrame({"key": ['K0', 'K1', 'K2', 'K4'], 'A': ['A0', 'A1', 'A2', 'A3'],
                     "B": ['I2', 'I3', 'I4', 'I5']}, index=['I0', 'I1', 'I2', 'I3'])
right = pd.DataFrame({"key": ['K0', 'K1', 'K2', 'K3'], 'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']}, index=['I0', 'I2', 'I3', 'I4'])
print(left)
print(right)
# 通过on参数进行merge
m1 = pd.merge(left, right, on='key')
print(m1)
# 指定求并集
m2 = pd.merge(left, right, on='key', how='outer')
print(m2)
# 指定left_on，right_on
m3 = pd.merge(left, right, left_on='key', right_on='key', how='right')
print(m3)
# 指定left_on，right_index
m4 = pd.merge(left, right, left_on='B', right_index=True)
print(m4)
