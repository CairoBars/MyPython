#_*_coding:utf-8_*_
import pygame
class Ship():
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置初始位置"""
		self.screen=screen
		self.ai_settings=ai_settings
		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images\ship.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.moving_right=False
		self.moving_left=False

		#将每艘飞船放在屏幕低部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		#在飞船的属性center中存储小数值
		self.center=float(self.rect.centerx)

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect )

	def update(self):
		'''
		if self.moving_right:
			self.rect.centerx+=1
		elif self.moving_left:
			self.rect.centerx-=1
		'''
		#更新飞船的center值，因为更精确，而不是rect，因为rect和centerx等属性只能存储整数值
		if self.moving_left and self.rect.left>0:
			self.center-=self.ai_settings.ship_speed_factor
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor

		self.rect.centerx=self.center