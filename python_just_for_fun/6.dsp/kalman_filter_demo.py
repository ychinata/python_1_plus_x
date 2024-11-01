# -*- coding=utf-8 -*-
# Kalman filter example demo in Python

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html
# by Andrew D. Straw

# xy. 2023.1.10
import numpy
# import pylab
import matplotlib.pyplot as pylab
import math
# import matplotlib
# matplotlib.usr(“TkAgg”)

# 图像上显示中文
pylab.rcParams['font.sans-serif'] = ['SimHei']


# 这里是假设A=1，H=1的情况

# 参数初始化1
# n_iter = 50
# sz = (n_iter,)  # size of array
# x = -0.37727  # 真实值
# Q = 1e-5    # 过程方差
# R = 0.01     # 测量方差
# x_hat_init_value = 0.0

# 参数初始化2
n_iter = 100
sz = (n_iter,)  # size of array
x = 24  # 真实值
Q = 4e-4    # 过程方差
R = 0.25     # 测量方差
x_hat_init_value = 23.5

z = numpy.random.normal(x, math.sqrt(R), size=sz)  # 观测值 ,观测时存在噪声

# 分配数组空间
xhat = numpy.zeros(sz)  # x 滤波估计值
P = numpy.zeros(sz)  # 滤波估计协方差矩阵
xhatminus = numpy.zeros(sz)  # x 估计值
Pminus = numpy.zeros(sz)  # 估计协方差矩阵
K = numpy.zeros(sz)  # 卡尔曼增益

# R = 0.1 ** 2  # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = x_hat_init_value
P[0] = 1.0

for k in range(1, n_iter):
    # 预测
    xhatminus[k] = xhat[k - 1]  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
    Pminus[k] = P[k - 1] + Q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

    # 更新
    K[k] = Pminus[k] / (Pminus[k] + R)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
    xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
    P[k] = (1 - K[k]) * Pminus[k]  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1

pylab.figure()
pylab.plot(z, 'k+', label='温度计的测量结果')  # 观测值
pylab.plot(xhat, 'b-', label='卡尔曼滤波后验估计')  # 滤波估计值
pylab.axhline(x, color='g', label='真实值')  # 真实值
pylab.legend()
pylab.xlabel('时间(分钟)')
pylab.ylabel('温度')

pylab.figure()
valid_iter = range(1, n_iter)  # Pminus not valid at step 0
pylab.plot(valid_iter, Pminus[valid_iter], label='a priori error estimate')
pylab.xlabel('时间(分钟)')
pylab.ylabel('$℃^2$')
pylab.setp(pylab.gca(), 'ylim', [0, R])
pylab.show()
