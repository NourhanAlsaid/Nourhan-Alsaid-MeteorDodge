import pygame,sys
pygame.init()
pygame.mixer.init()
# screen setting
WIDTH = 480
HEIGHT = 800
screen = pygame.display.set_mode((480, 800))
FBS = 60
MY_Meteor_EVENT = pygame.USEREVENT + 1
# background colors
black = (0,0,0)
white = (255,255,255)
#player setting
player_speed = 12
player_image = "img/player_sprite.png"
player_death_sound = "audio/player_dead.ogg"
#meteor speed
Meteor_speeds = {"big": 10, "medium":11, "small": 12, "tiny":12}
Meteor_images = {"big":["img/meteor_big_1.png", "img/meteor_big_2.png", "img/meteor_big_3.png", "img/meteor_big_4.png"],
                 "medium":["img/meteor_med_1.png", "img/meteor_med_2.png"],
                 "small": ["img/meteor_small_1.png" ,"img/meteor_small_2.png"],
                 "tiny": ["img/meteor_tiny_2.png","img/meteor_tiny_1.png"] }

Meteor_spawn_sounds = ["audio/spawn_sound_1.ogg" , "audio/spawn_sound_2.ogg" , "audio/spawn_sound_3.ogg" , "audio/player_dead.ogg"]
background = "img/bg.png"
