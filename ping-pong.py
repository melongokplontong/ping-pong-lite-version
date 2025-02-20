from pygame import*

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_p1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_p2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
raket1 = Player('putuyraket.png', 30, 200, 4, 50, 150)
raket2 = Player('putuyraket.png', 520, 200, 4, 50, 150)
bola = GameSprite('putuybola.png', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3
finish = False
font.init()
font = font.Font(None, 35)
win1 = font.render('PLAYER 1 WIN', True, (180, 0, 0))
win2 = font.render('PLAYER 2 WIN', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        raket1.reset()
        raket2.reset()
        raket1.update_p1()
        raket2.update_p2()
        bola.reset()


        bola.rect.x += speed_x
        bola.rect.y += speed_y


        if sprite.collide_rect(raket1, bola) or sprite.collide_rect(raket2, bola):
            speed_x *= -1

        if bola.rect.y > win_height-50 or bola.rect.y <0:
            speed_y *= -1
        if bola.rect.x < 0:
            window.blit(win2, (200, 200))
            finish = True
        if bola.rect.x > win_width:
            window.blit(win1, (200, 200))
            finish = True
    display.update()
    clock.tick(FPS)