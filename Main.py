import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Musique/Fort Boyard Main Theme.mp3")
pygame.mixer.music.set_volume(0.5)  # Régle le volume entre 0.0 et 1.0
pygame.mixer.music.play(-1)  # -1 pour jouer la musique en boucle

#genere la fenètre de notre jeu
pygame.display.set_caption("The maze")
screen = pygame.display.set_mode ((1200,700))


background = pygame.image.load("Images/Image d'accueil.jpg")
#import charger notre bouton pour lancer la partie
fond_ecran_menu = pygame.image.load('Images/Bouton Play.PNG')
play_button_menu = pygame.transform.scale(fond_ecran_menu,(300,300))
quit_button_image = pygame.image.load('Images/Bouton Quitter.PNG')
quit_button_image = pygame.transform.scale(quit_button_image, (300,240))

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))

#perso = pygame.image.load("").convert_alpha()
#position_perso = perso.get_rect()
#screen.blit(perso, (200,300))

running = True
game_running = False
#boucle tant que cette condition est vrai

while running:

    screen.blit(background, (0, 0))
    screen.blit(play_button_menu, play_button_rect)
    screen.blit(quit_button_image, quit_button_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture du jeu")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                print("Lancer le jeu")
                game_running = True
                running = False

            if quit_button_rect.collidepoint(event.pos):
                running = False
                print("Quitter le jeu")

pygame.quit()
