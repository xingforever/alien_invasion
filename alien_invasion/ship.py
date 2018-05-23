import pygame

class Ship:
    def __init__(self, ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像获取外接矩形
        self.image=pygame.image.load(r'D:\\Python\\alien_invasion\\alien_invasion\\alien_invasion\\images\\ship.bmp')      
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center= float(self.rect.centerx)
        #移动标志
        self.moving_right =False
        self.moving_left=False
  
    def update(self):
        if self.moving_right == True  and self.rect.right<self.screen_rect.right:
            self.center +=(float)(self.ai_settings.ship_speed_factor)
        if self.moving_left ==True and  self.rect.left>0:
            self.center -=(float)(self.ai_settings.ship_speed_factor)

        self.rect.centerx = self.center 

    def blitme(self):
        #指定位置绘制飞船
        self.screen.blit(self.image,self.rect)



       
