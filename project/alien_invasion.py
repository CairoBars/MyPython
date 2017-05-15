#_*_coding:utf-8_*_

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.bullet_width,ai_settings.bullet_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings,screen)
	bullets=Group()
	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		#gf.check_events(ai_settings,screen,ship,bullets)
		#ship.update()
		#bullets.update()
		'''
		for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)
				'''
		#print(len(bullets))
		#gf.update_screen(ai_settings,screen,ship,bullets)
		pass



run_game()