import pygame
pygame.init()

#genere la fenètre de notre jeu
pygame.display.set_caption("The maze")
screen = pygame.display.set_mode ((1200,700))


background = pygame.image.load("IMAGE BG ACCUEIL.jpg")

perso = pygame.image.load("mario test.png").convert_alpha()
position_perso = perso.get_rect()
screen.blit(perso, (200,300))

running = True

#boucle tant que cette condition est vrai

while running:

    screen.blit(background, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print ("Fermeture du jeu")