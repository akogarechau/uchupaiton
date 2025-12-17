import pygame
import random
import time
from pathlib import Path
import math

# Константы игры
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
BG_COLOR = (0, 0, 20)
IMAGES_DIR = Path(__file__).parent

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, image_path, screen_w, screen_h):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h
        
        full_path = IMAGES_DIR / image_path
        try:
            self.image = pygame.image.load(full_path).convert_alpha()
        except:
            self.image = pygame.Surface((width, height))
            self.image.fill((100, 100, 100))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

class PlayerShip(BaseSprite):
    def __init__(self, screen_w, screen_h):
        super().__init__(120, 100, "ship.png", screen_w, screen_h)
        self.rect.centerx = screen_w // 2
        self.rect.bottom = screen_h - 60
        self.speed = 400
        self.bullet_speed = 300
        self.last_shot = 0
        self.shot_delay = 0.3
        self.keys = {
            'left': pygame.K_LEFT, 
            'right': pygame.K_RIGHT, 
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'shoot': pygame.K_SPACE
        }
        self.killed_enemies = 0

    def reset(self):
        self.rect.centerx = self.screen_w // 2
        self.rect.bottom = self.screen_h - 60
        self.speed = 400
        self.bullet_speed = 300
        self.shot_delay = 0.3
        self.last_shot = 0
        self.killed_enemies = 0

    def update(self, dt, pressed_keys):
        move_x = 0
        move_y = 0
        
        if pressed_keys[self.keys['left']]:
            move_x -= self.speed * dt
        if pressed_keys[self.keys['right']]:
            move_x += self.speed * dt
        if pressed_keys[self.keys['up']]:
            move_y -= self.speed * dt
        if pressed_keys[self.keys['down']]:
            move_y += self.speed * dt
        
        self.rect.x = max(0, min(self.rect.x + move_x, self.screen_w - self.rect.width))
        self.rect.y = max(100, min(self.rect.y + move_y, self.screen_h - self.rect.height))
        
        if (pressed_keys[self.keys['shoot']] and 
            time.time() - self.last_shot > self.shot_delay):
            bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_speed)
            self.last_shot = time.time()
            return bullet
        return None

    def apply_powerup(self):
        effect = random.randint(1, 3)
        if effect == 1:
            self.bullet_speed = min(self.bullet_speed * 1.5, 600)
        elif effect == 2:
            self.shot_delay = max(self.shot_delay * 0.7, 0.15)
        else:
            self.speed = min(self.speed * 1.2, 700)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((20, 40))
        self.image.fill((0, 255, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self, dt):
        self.rect.y -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, image_path, speed_range, screen_w, screen_h, is_bonus=False):
        super().__init__()
        self.is_bonus = is_bonus
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.size = size
        
        full_path = IMAGES_DIR / image_path
        try:
            original_image = pygame.image.load(full_path).convert_alpha()
        except:
            original_image = pygame.Surface(size)
            color = (255, 100, 100) if is_bonus else (150, 150, 150)
            original_image.fill(color)
        
        # НОВОЕ: СЛУЧАЙНЫЙ ПОВОРОТ астероида (от -45° до +45°)
        self.rotation = random.uniform(-math.pi/4, math.pi/4)  # -45° до +45° в радианах
        self.image = pygame.transform.rotate(
            pygame.transform.scale(original_image, size), 
            math.degrees(self.rotation)
        )
        
        # УМЕНЬШЕННЫЙ ХИТБОКС (на 20% меньше визуального размера)
        hitbox_size = (int(size[0] * 0.8), int(size[1] * 0.8))
        self.rect = self.rect = pygame.Rect(0, 0, *hitbox_size)
        self.rect.center = self.image.get_rect().center  # Центрируем хитбокс
        
        self.reset_position()
        self.speed = random.randint(*speed_range) if isinstance(speed_range, tuple) else speed_range

    def reset_position(self):
        channel_size = self.screen_w // 10
        self.rect.x = random.randint(0, 9) * channel_size + (channel_size // 4)
        self.rect.bottom = -50

    def update(self, dt):
        self.rect.y += self.speed * dt
        if self.rect.top > self.screen_h:
            self.reset_position()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Космический стрелок")
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)
    
    game_state = "playing"
    enemies_destroyed = 0
    total_enemies = 200
    
    enemies = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    player = PlayerShip(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    for _ in range(40):
        enemy = Enemy((80, 80), "asteroid.png", (80, 150), SCREEN_WIDTH, SCREEN_HEIGHT)
        enemies.add(enemy)
    
    for _ in range(3):
        bonus = Enemy((60, 60), "bonus.png", 100, SCREEN_WIDTH, SCREEN_HEIGHT, True)
        bonuses.add(bonus)
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        pressed_keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game_state == "game_over" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = "playing"
                    enemies_destroyed = 0
                    player.reset()
                    for enemy in enemies:
                        enemy.reset_position()
                    for bonus in bonuses:
                        bonus.reset_position()
                    bullets.empty()
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        if game_state == "playing":
            new_bullet = player.update(dt, pressed_keys)
            if new_bullet:
                bullets.add(new_bullet)
            
            enemies.update(dt)
            bonuses.update(dt)
            bullets.update(dt)
            
            for bullet in bullets.copy():
                hits = pygame.sprite.spritecollide(bullet, enemies, True)
                if hits:
                    enemies_destroyed += len(hits)
                    player.killed_enemies += len(hits)
                    bullet.kill()
                    new_enemy = Enemy((80, 80), "asteroid.png", (80, 150), SCREEN_WIDTH, SCREEN_HEIGHT)
                    enemies.add(new_enemy)
            
            if pygame.sprite.spritecollide(player, enemies, False):
                game_state = "game_over"
            
            bonus_hits = pygame.sprite.spritecollide(player, bonuses, True)
            if bonus_hits:
                player.apply_powerup()
                new_bonus = Enemy((60, 60), "bonus.png", 100, SCREEN_WIDTH, SCREEN_HEIGHT, True)
                bonuses.add(new_bonus)
            
            if enemies_destroyed >= total_enemies:
                game_state = "playing"
                enemies_destroyed = 0
                player.reset()
                for enemy in enemies:
                    enemy.reset_position()
                for bonus in bonuses:
                    bonus.reset_position()
                bullets.empty()
        
        # Отрисовка
        screen.fill(BG_COLOR)
        
        if game_state == "playing":
            enemies.draw(screen)
            bonuses.draw(screen)
            bullets.draw(screen)
            screen.blit(player.image, player.rect)
        
        elif game_state == "game_over":
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(150)
            overlay.fill((100, 20, 20))
            screen.blit(overlay, (0, 0))
            enemies.draw(screen)
            bonuses.draw(screen)
            bullets.draw(screen)
            screen.blit(player.image, player.rect)
        
        # Надписи на переднем плане
        score_text = font.render(f"Астероидов: {player.killed_enemies}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(20, 20))
        screen.blit(score_text, score_rect)
        
        progress_text = small_font.render(f"/ {total_enemies}", True, (255, 255, 255))
        progress_rect = score_text.get_rect(topleft=(score_rect.right + 10, 25))
        screen.blit(progress_text, progress_rect)
        
        if game_state == "game_over":
            gameover_text = font.render("GAME OVER", True, (255, 255, 255))
            gameover_rect = gameover_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(gameover_text, gameover_rect)
            
            final_score_text = font.render(f"Уничтожено: {player.killed_enemies}", True, (255, 255, 255))
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(final_score_text, final_score_rect)
            
            restart_text = small_font.render("SPACE - Рестарт, ESC - Выход", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
