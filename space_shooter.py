import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("太空射击游戏 - 控制飞船移动和射击")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 50)

# 玩家飞船类
class Player:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 100
        self.speed = 5
        self.color = BLUE
        self.health = 100
        self.score = 0
        self.bullets = []
        self.shoot_cooldown = 0
        
    def draw(self):
        # 绘制飞船主体
        pygame.draw.polygon(screen, self.color, [
            (self.x + self.width//2, self.y),  # 顶部
            (self.x, self.y + self.height),    # 左下
            (self.x + self.width, self.y + self.height)  # 右下
        ])
        
        # 绘制飞船引擎
        pygame.draw.rect(screen, YELLOW, 
                         (self.x + 15, self.y + self.height, 10, 10))
        
        # 绘制生命值条
        health_width = 40
        health_height = 5
        health_fill = (self.health / 100) * health_width
        pygame.draw.rect(screen, RED, 
                         (self.x, self.y - 10, health_width, health_height))
        pygame.draw.rect(screen, GREEN, 
                         (self.x, self.y - 10, health_fill, health_height))
        
        # 绘制所有子弹
        for bullet in self.bullets:
            bullet.draw()
    
    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            
        # 边界检查
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))
        
        # 射击冷却
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def shoot(self):
        if self.shoot_cooldown == 0:
            bullet_x = self.x + self.width // 2 - 2
            bullet_y = self.y
            self.bullets.append(Bullet(bullet_x, bullet_y))
            self.shoot_cooldown = 10  # 射击冷却时间
    
    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)

# 子弹类
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 4
        self.height = 12
        self.speed = 8
        self.color = GREEN
    
    def draw(self):
        pygame.draw.rect(screen, self.color, 
                         (self.x, self.y, self.width, self.height))
    
    def move(self):
        self.y -= self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# 敌人类
class Enemy:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = random.uniform(1.0, 3.0)
        self.color = RED
        self.health = 1
    
    def draw(self):
        # 绘制敌人（简单的正方形）
        pygame.draw.rect(screen, self.color, 
                         (self.x, self.y, self.width, self.height))
        
        # 绘制敌人眼睛
        pygame.draw.circle(screen, WHITE, 
                          (self.x + 8, self.y + 10), 4)
        pygame.draw.circle(screen, WHITE, 
                          (self.x + self.width - 8, self.y + 10), 4)
        pygame.draw.circle(screen, BLACK, 
                          (self.x + 8, self.y + 10), 2)
        pygame.draw.circle(screen, BLACK, 
                          (self.x + self.width - 8, self.y + 10), 2)
    
    def move(self):
        self.y += self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# 游戏主类
class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.enemy_spawn_rate = 60  # 每60帧生成一个敌人
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()
        self.fps = 60
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.player.shoot()
                
                # 重新开始游戏
                if event.key == pygame.K_r and self.game_over:
                    self.__init__()  # 重置游戏
        
        # 持续按键检测
        keys = pygame.key.get_pressed()
        if not self.game_over:
            self.player.move(keys)
    
    def spawn_enemies(self):
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= self.enemy_spawn_rate:
            self.enemies.append(Enemy())
            self.enemy_spawn_timer = 0
            
            # 逐渐增加难度
            if self.player.score > 50:
                self.enemy_spawn_rate = max(30, 60 - self.player.score // 10)
    
    def update(self):
        if self.game_over:
            return
            
        # 更新玩家子弹
        self.player.update_bullets()
        
        # 生成敌人
        self.spawn_enemies()
        
        # 更新敌人位置
        for enemy in self.enemies[:]:
            enemy.move()
            
            # 检查敌人是否超出屏幕
            if enemy.y > HEIGHT:
                self.enemies.remove(enemy)
                self.player.health -= 5  # 敌人逃脱扣血
                if self.player.health <= 0:
                    self.game_over = True
            
            # 检查子弹与敌人碰撞
            for bullet in self.player.bullets[:]:
                if enemy.get_rect().colliderect(bullet.get_rect()):
                    self.player.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.player.score += 10
                    break
            
            # 检查玩家与敌人碰撞
            player_rect = pygame.Rect(self.player.x, self.player.y, 
                                     self.player.width, self.player.height)
            if enemy.get_rect().colliderect(player_rect):
                self.enemies.remove(enemy)
                self.player.health -= 20
                if self.player.health <= 0:
                    self.game_over = True
    
    def draw_ui(self):
        # 绘制分数
        score_text = self.font.render(f"分数: {self.player.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # 绘制生命值
        health_text = self.font.render(f"生命值: {self.player.health}", True, WHITE)
        screen.blit(health_text, (10, 50))
        
        # 绘制控制说明
        controls = [
            "控制说明:",
            "W/A/S/D 或 方向键: 移动飞船",
            "空格键: 射击",
            "R键: 重新开始游戏"
        ]
        
        for i, text in enumerate(controls):
            control_text = self.small_font.render(text, True, WHITE)
            screen.blit(control_text, (WIDTH - 250, 10 + i * 25))
        
        # 游戏结束画面
        if self.game_over:
            # 半透明覆盖层
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            # 游戏结束文本
            game_over_text = self.font.render("游戏结束!", True, RED)
            final_score_text = self.font.render(f"最终分数: {self.player.score}", True, YELLOW)
            restart_text = self.small_font.render("按 R 键重新开始游戏", True, WHITE)
            
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
            screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2))
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))
    
    def draw(self):
        # 绘制星空背景
        screen.fill(BLACK)
        
        # 绘制一些星星
        for _ in range(50):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            size = random.randint(1, 3)
            brightness = random.randint(150, 255)
            pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)
        
        # 绘制游戏对象
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        # 绘制UI
        self.draw_ui()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)

# 主程序入口
if __name__ == "__main__":
    print("太空射击游戏启动中...")
    print("游戏控制:")
    print("  - W/A/S/D 或方向键: 移动飞船")
    print("  - 空格键: 射击")
    print("  - R键: 重新开始游戏")
    print("\n游戏目标:")
    print("  - 射击红色敌人获得分数")
    print("  - 避免敌人碰撞和逃脱")
    print("  - 生命值降到0游戏结束")
    print("\n祝你好运!")
    
    game = Game()
    game.run()