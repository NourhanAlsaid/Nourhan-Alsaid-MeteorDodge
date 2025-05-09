import pygame, sys, random
from config import *
from Meteor import Meteor
from Player import Player

#main game loop
def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meteor Dodge") # add the game name

    pygame.time.set_timer(MY_Meteor_EVENT, 1000) #add time in milliseconds

    clock = pygame.time.Clock()

    # player lose setting
    font = pygame.font.Font(None, 48)
    player_lose = font.render("You Lost!", True, white)
    player_lose_rect = player_lose.get_rect(center=(WIDTH//2, HEIGHT//2))
    player_lose_screen = pygame.Surface((WIDTH, HEIGHT))
    player_lose_screen.set_alpha(100)
    player_lose_screen.fill(black)


    # upload the background image
    background = pygame.image.load("img/bg.png").convert()

    #create Meteors
    meteors = []
    #initialize player
    player = Player()

    # running the main game loop
    while True:
        keys = pygame.key.get_pressed()

        #quit game with either exit or ESC key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

            #initialize meteor event
            if event.type == MY_Meteor_EVENT:
                meteor = Meteor()
                meteors.append(meteor)
                meteor.spawn_sound.play()
                # setting timer
                pygame.time.set_timer(MY_Meteor_EVENT, random.randint(800, 1500))

        # fill screen background
        screen.blit(background, (0,0))

        #meteor movements, logics
        for meteor in meteors[:]:
            meteor.fall()
            meteor.draw(screen)

            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)

            # the events of character death
            if player.alive and meteor.rect.colliderect(player.rect):
                player.deadSound.play()
                player.alive = False


        #calling movement and image from payer file
        if player.alive:
            # add keys to the player
            keys = pygame.key.get_pressed()
            player.move(keys)
            player.draw(screen)
        else:
            screen.blit(player_lose_screen, (0,0))
            screen.blit(player_lose, player_lose_rect)

        pygame.display.flip()
        clock.tick(FBS) #FBS from the Config file



if __name__ == "__main__":
    main()

