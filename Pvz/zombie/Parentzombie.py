import abc


class ParentZombie(object):
    def __init__(self, screen, x, y, image, life, damage):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.life = life
        self.damage = damage
        self.headFlag = True

    def outOfBounds(self):
        return self.x < 100

    @abc.abstractmethod
    def step(self, sets):
        pass

    # 殭屍圖片
    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 子彈擊中殭屍
    def hitBy(self, bt):
        # 1.獲取子彈座標
        btX = bt.x
        btY = bt.y
        btXW = bt.x + bt.width
        btYH = bt.y + bt.height
        # 2.獲取殭屍座標
        fX = self.x + self.width/2
        fY = self.y
        fXW = self.x + self.width
        fYH = self.y + self.height
        # 3.判斷是否擊中
        return fX >= btX-2 and fX <= btX+1.5 and fY < btY and fYH > btYH
