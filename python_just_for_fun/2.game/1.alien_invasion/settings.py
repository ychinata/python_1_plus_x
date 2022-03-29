# first pygame: alien invasion
# 2022.3.27
# Python编程_从入门到实践.Python Crash Course.[美]埃里克·马瑟斯
# Project 1

class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 2
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

