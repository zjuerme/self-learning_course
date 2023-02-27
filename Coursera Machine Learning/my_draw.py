import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块
def logarithm_func(x): #定义熵函数
    y=-x*math.log(x, 2)-(1-x)*math.log(1-x,2)
    return y

def draw_entropy():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    fig=plt.figure(figsize=(6,4)) #新建画布
    ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax) #将绘图区对象添加到画布中
    X=np.linspace(0.01, 0.99, 100) #构造自变量组
    Y=[logarithm_func(x) for x in X] #求函数值
    ax.plot(X, Y, label=r'$0<a<1$') #绘制指数函数
    ax.scatter(0.5, 1, color='red')
    ax.annotate(text=r'$H(x) = -x {log}_2(x) - (1- x) {log}_2(1- x)$', xy=(2/5, 3/4), xytext=(2/5, 3/4))
    plt.legend()
    plt.show()

