#_*_coding:utf-8_*_
class Settings():
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设定
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(200,200,200)
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=1
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullets_allowed=3
