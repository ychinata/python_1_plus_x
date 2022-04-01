# first pygame
# 2022.3.27
# Python编程_从入门到实践.Python Crash Course.[美]埃里克·马瑟斯
# Project 1

import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

"""管理游戏资源和行为的类"""
class AlienInvasion:
    """初始化游戏并创建游戏资源"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # 游戏不全屏，指定窗口大小
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        # 游戏全屏
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # 飞船
        self.ship = Ship(self)
        # 子弹
        self.bullets = pygame.sprite.Group()
        # 外星人
        self.aliens = pygame.sprite.Group()
        self._creat_fleet()
        # 设置背景色
        self.bg_color = (230, 230, 230)

    """开始游戏主循环"""
    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            self._check_events_()
            self.ship.update()
            self._update_bullets()

            # 每次循环时都重绘屏幕
            self._update_screen()

    # 辅助方法命名以_开头
    """监视键盘和鼠标事件"""
    def _check_events_(self):
        for event in pygame.event.get():
            # 点击窗口关闭，退出游戏
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 松开左右键停止移动飞船
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """响应按键按下"""
    def _check_keydown_events(self, event):
        # 系统时如何同时检测到左右键同时按下的？
        # 按下左右键移动飞船
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按下Q键退出游戏
        elif event.key == pygame.K_q:
            sys.exit()
        # 按下空格键发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    """响应按键松开"""
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    """创建一颗子弹，并将其加入编组bullets中"""
    def _fire_bullet(self):
        # 限制子弹数量
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """更新子弹的位置并删除消失的子弹"""
    def _update_bullets(self):
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    """创建外星人群"""
    def _creat_fleet(self):
        # 创建一个外星人
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            self._creat_alien(alien_number)

    """创建一个外星人并将其放在当前行"""
    def _creat_alien(self, alien_number):
        # 创建一个外星人并将其加入当前行
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    """每次循环时都重绘屏幕"""
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()

