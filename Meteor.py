import pygame
import config
import random

from config import Meteor_images, Meteor_spawn_sounds, WIDTH


class  Meteor:
    def __init__(self):
        self.type = random.choice(list(config.Meteor_speeds.keys()))
        self.speed = config.Meteor_speeds[self.type]
        sprite_choice = random.choice(Meteor_images[self.type])
        self.sprite = pygame.image.load(sprite_choice).convert_alpha()
        self.rect = self.sprite.get_rect()
        rand_sound = random.choice(Meteor_spawn_sounds)
        self.spawn_sound = pygame.mixer.Sound(rand_sound)
        width = WIDTH
        screen_x = (random.randint(0, width - self.rect.width))
        self.rect.topleft = (screen_x, 0)

    def fall (self):
        self.rect = self.rect.move(0, self.speed)
    def draw (self, surface):
        surface.blit(self.sprite, self.rect)
