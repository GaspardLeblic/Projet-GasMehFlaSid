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
            print ("Fermeture du jeu")
pygame.quit()
///////////////////////////////////////

import pygame

pygame.init()

pygame.display.set_caption("The maze")
screen = pygame.display.set_mode((1200, 700))

background = pygame.image.load("IMAGE BG ACCUEIL.jpg")
perso = pygame.image.load("mario test.png").convert_alpha()
position_perso = perso.get_rect()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)

font = pygame.font.SysFont('Arial', 30)
title_font = pygame.font.SysFont('Arial', 50)

description = "Bienvenue dans le jeu ! Cliquez sur Jouer pour commencer."

screen.blit(perso, (200, 300))

def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

running = True
game_started = False

while running:
    screen.blit(background, (0, 0))

    title_text = title_font.render("The Maze", True, WHITE)
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))
    
    description_text = font.render(description, True, WHITE)
    screen.blit(description_text, (screen.get_width() // 2 - description_text.get_width() // 2, 150))

    draw_button("Jouer", 450, 400, 200, 50)
    draw_button("Quitter", 450, 500, 200, 50)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture du jeu")
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            if 450 <= mouse_x <= 650 and 400 <= mouse_y <= 450:
                game_started = True
                description = "Le jeu commence !"
                print("Jeu commencé !")
                
            elif 450 <= mouse_x <= 650 and 500 <= mouse_y <= 550:
                running = False
                print("Fermeture du jeu")

    if game_started:

        screen.blit(perso, (200, 300))

        pygame.display.flip()

pygame.quit()
