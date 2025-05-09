import pygame
import config
class Player:
    def __init__(self):
        self.speed = config.player_speed
        self.sprite =pygame.image.load(config.player_image)
        self.rect = self.sprite.get_rect()
        self.rect.x = config.WIDTH // 2 - self.rect.width // 2
        self.rect.y = config.HEIGHT - self.rect.height - 20
        self.alive = True
        self.deadSound = pygame.mixer.Sound(config.player_death_sound)
    def move (self,keys):
        if keys[pygame.K_a]:
           if self.rect.left > 0:
               self.rect = self.rect.move(-12, 0 )

        elif keys[pygame.K_d]:
            if self.rect.right < 480:
                self.rect = self.rect.move(12, 0)
    def draw (self, surface):
        surface.blit(self.sprite, self.rect)




