import pygame
import random
import math
import time

# 初始化Pygame
pygame.init()

# 设置窗口大小
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("坦克 VS Boss")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 加载图片
tank_img = pygame.image.load('tank.png').convert_alpha()
boss_img = pygame.image.load('boss.png').convert_alpha()
background_img = pygame.image.load('background.png').convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# 坦克类
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(tank_img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 7
        self.health = 100
        self.last_shot = 0
        self.shot_delay = 200
        self.damage_dealt = 0
        self.can_use_special = False
        self.clear_screen_count = 3
        self.last_space_press = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE]:
            if now - self.last_space_press < 200:  # 双击间隔200毫秒
                self.clear_screen()
            self.last_space_press = now

        if keys[pygame.K_SPACE] and now - self.last_shot > self.shot_delay:
            self.shoot()
            self.last_shot = now

        if self.damage_dealt >= 500:
            self.can_use_special = True

    def shoot(self):
        bullet = TankBullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        tank_bullets.add(bullet)

    def special_attack(self):
        if self.can_use_special:
            special = SpecialAttack(self.rect.centerx, self.rect.top)
            all_sprites.add(special)
            tank_bullets.add(special)
            self.can_use_special = False
            self.damage_dealt = 0

    def clear_screen(self):
        if self.clear_screen_count > 0:
            for bullet in boss_bullets:
                bullet.kill()
            self.clear_screen_count -= 1

# Boss类
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(boss_img, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.top = 20
        self.health = 1000
        self.speed = random.randint(2, 6)
        self.direction = 1
        self.last_shot = 0
        self.shot_delay = 500
        self.damage_dealt = 0
        self.laser_active = False
        self.laser_start_time = 0

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.direction *= -1
            self.speed = random.randint(2, 6)

        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shot_delay:
            self.shoot()
            self.last_shot = now

        if self.damage_dealt >= 20 and not self.laser_active:
            self.activate_laser()

        if self.laser_active and now - self.laser_start_time > 2000:  # 2秒后停止激光
            self.laser_active = False

    def shoot(self):
        for i in range(8):
            angle = i * (2 * math.pi / 8)
            bullet = BossBullet(self.rect.centerx, self.rect.bottom, angle)
            all_sprites.add(bullet)
            boss_bullets.add(bullet)

    def activate_laser(self):
        self.laser_active = True
        self.laser_start_time = pygame.time.get_ticks()
        self.damage_dealt = 0

# 坦克子弹类
class TankBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -15

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Boss子弹类
class BossBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 5
        self.vx = math.cos(angle) * self.speed
        self.vy = math.sin(angle) * self.speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > HEIGHT or self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

# 特殊攻击类
class SpecialAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# 创建精灵组
all_sprites = pygame.sprite.Group()
tank_bullets = pygame.sprite.Group()
boss_bullets = pygame.sprite.Group()

tank = Tank()
boss = Boss()
all_sprites.add(tank, boss)

# 游戏主循环
def game_loop():
    global running, damage_dealt
    running = True
    clock = pygame.time.Clock()
    start_time = time.time()
    damage_dealt = 0

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # 鼠标右键
                    tank.special_attack()

        # 更新
        all_sprites.update()

        # 碰撞检测
        hits = pygame.sprite.spritecollide(tank, boss_bullets, True)
        for hit in hits:
            tank.health -= 10
            boss.damage_dealt += 10
            if tank.health <= 0:
                return "GAME OVER"

        if boss.laser_active:
            if tank.rect.left < boss.rect.centerx < tank.rect.right:
                tank.health -= 15 / 60  # 每帧减少0.25血量，相当于每秒15

        hits = pygame.sprite.spritecollide(boss, tank_bullets, True)
        for hit in hits:
            if isinstance(hit, SpecialAttack):
                boss.health -= 200
            else:
                boss.health -= 10
            damage_dealt += 10
            tank.damage_dealt += 10
            if boss.health <= 0:
                return "WIN"

        # 绘制
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)

        # 绘制激光
        if boss.laser_active:
            pygame.draw.line(screen, RED, (boss.rect.centerx, boss.rect.bottom), (boss.rect.centerx, HEIGHT), 5)

        # 显示血量和其他信息
        font = pygame.font.Font(None, 36)
        tank_health_text = font.render(f"Tank: {int(tank.health)}", True, GREEN)
        boss_health_text = font.render(f"Boss: {boss.health}", True, RED)
        damage_text = font.render(f"Damage: {tank.damage_dealt}", True, YELLOW)
        clear_screen_text = font.render(f"Clear Screen: {tank.clear_screen_count}", True, BLUE)
        screen.blit(tank_health_text, (10, 10))
        screen.blit(boss_health_text, (WIDTH - 150, 10))
        screen.blit(damage_text, (10, 50))
        screen.blit(clear_screen_text, (10, 90))

        pygame.display.flip()

def show_end_screen(result):
    screen.blit(background_img, (0, 0))
    font = pygame.font.Font(None, 74)
    if result == "WIN":
        text = font.render("WIN!", True, GREEN)
    else:
        text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 36)
    time_text = font.render(f"Time: {int(time.time() - start_time)} seconds", True, BLUE)
    damage_text = font.render(f"Damage dealt: {damage_dealt}", True, BLUE)
    screen.blit(time_text, (WIDTH/2 - 100, HEIGHT/2 + 50))
    screen.blit(damage_text, (WIDTH/2 - 100, HEIGHT/2 + 100))

    restart_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 150, 200, 50)
    quit_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 220, 200, 50)

    pygame.draw.rect(screen, GREEN, restart_button)
    pygame.draw.rect(screen, RED, quit_button)

    font = pygame.font.Font(None, 32)
    restart_text = font.render("Restart", True, WHITE)
    quit_text = font.render("Quit", True, WHITE)
    screen.blit(restart_text, (restart_button.x + 70, restart_button.y + 15))
    screen.blit(quit_text, (quit_button.x + 80, quit_button.y + 15))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "RESTART"
                elif quit_button.collidepoint(event.pos):
                    return "QUIT"

def show_start_screen():
    screen.blit(background_img, (0, 0))
    font = pygame.font.Font(None, 74)
    title = font.render("Tank VS Boss", True, YELLOW)
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
    screen.blit(title, title_rect)

    start_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 50, 200, 50)
    pygame.draw.rect(screen, GREEN, start_button)

    font = pygame.font.Font(None, 32)
    start_text = font.render("Start Game", True, WHITE)
    screen.blit(start_text, (start_button.x + 50, start_button.y + 15))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "START"

# 主游戏循环
while True:
    action = show_start_screen()
    if action == "QUIT":
        break
    elif action == "START":
        while True:
            result = game_loop()
            if result == "QUIT":
                pygame.quit()
                exit()
            action = show_end_screen(result)
            if action == "QUIT":
                break
            elif action == "RESTART":
                # 重置游戏状态
                all_sprites.empty()
                tank_bullets.empty()
                boss_bullets.empty()
                tank = Tank()
                boss = Boss()
                all_sprites.add(tank, boss)
                start_time = time.time()
                damage_dealt = 0
            else:
                break

pygame.quit()
