import pygame
pygame.init()

#genere la fenètre de notre jeu
pygame.display.set_caption("The maze")
screen = pygame.display.set_mode ((1200,700))


background = pygame.image.load("IMAGE BG ACCUEIL.jpg")
#import charger notre bouton pour lancer la partie
play_button = pygame.image.load('bouton play.PNG')
play_button = pygame.transform.scale(play_button,(500,500))

#perso = pygame.image.load("").convert_alpha()
#position_perso = perso.get_rect()
#screen.blit(perso, (200,300))

running = True

#boucle tant que cette condition est vrai

while running:

    screen.blit(background, (0, 0))
    screen.blit(play_button,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            print ("Fermeture du jeu")
pygame.quit()

