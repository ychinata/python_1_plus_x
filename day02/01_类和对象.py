# 芒果：一类
# 我吃芒果：一个 :
# 类：一系列事物对通称，同类事物必定有相同的特征
# 词有多个
# 对象是类中对具体表现形式
# 面向对象编程：有对象才能编程
# 编程
color = "红色"
# 方法：函数
print(color)
class Apple:
    # 一箱
    # 类属性：类变量
    count = 12
    # 调用：类名.变量名

    # 那个对象调用，就表示哪个对象
    # __init__:魔术方法：在创建对象的时候，不需要调用，自动执行
    def __init__(self,color):
        # 类中对一些特征属性
        self.color = color
        self.weight = 0.5

    # 方法
    def play(self,num):
        self.cs = 12
        print("下落{}".format(self.color))
        print("因为苹果，而改变了世界{}...".format(Apple.count))
        self.run()
        return num

    def run(self):
        print(self.cs)


# 对象:无数个
# 类名():创建对象
a = Apple("红苹果")
b = Apple("青苹果")
# 看到颜色
# 对象.属性名：调用属性
print(a.color)
print(b.color)
# 方法：对象.方法名():调用方法
a.play(12)
a.run()

# Dog类
# body_color
# kind
# play()
# eat()
