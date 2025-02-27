import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Musique/Fort Boyard Main Theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

pygame.display.set_caption("The maze")
screen = pygame.display.set_mode((1200, 700))

background = pygame.image.load("Images/Image d'accueil.jpg")
fond_ecran_menu = pygame.image.load('Images/Bouton Play.PNG')
play_button_menu = pygame.transform.scale(fond_ecran_menu, (300, 300))
quit_button_image = pygame.image.load('Images/Bouton Quitter.PNG')
quit_button_image = pygame.transform.scale(quit_button_image, (300, 240))

sprite_sol = pygame.image.load("Images/Image_sol.jpg")
sprite_mur = pygame.image.load("Images/Image_mur.jpg")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))

personnage_image = pygame.image.load("Images/Perso_de_face.png")
personnage_image = pygame.transform.scale(personnage_image, (40, 40))

ecran_victoire = pygame.image.load("Images/Thank_you_for_playing.png")
ecran_victoire = pygame.transform.scale(ecran_victoire, (1200, 700))

bouton_suivant_image = pygame.image.load("Images/Image_prochain_niveau.png")
bouton_suivant_rect = bouton_suivant_image.get_rect(center=(600, 600))

running = True
game_running = False
victoire = False
niveau = 1

def charger_labyrinthe(niveau):
    labyrinthes = [
        # Niveau 1
        [
            "111111111111111111111111",
            "100000000010000000000001",
            "101111111010111110111101",
            "101000100010000000000001",
            "101010101011011111101101",
            "100010001001010100000111",
            "101111111101010111110001",
            "101000000100010100011101",
            "100011110110110101010001",
            "111010000100100001010111",
            "100000111101101111010011",
            "101110110000001011011011",
            "101000000111111000001111",
            "111111111111111111111111",
    ],
        # Niveau 2
        [
            "111111111111111111111111",
            "100000000011111100000001",
            "101111110011111100111101",
            "101000010000000000001001",
            "101010111011101110101101",
            "100010000011100100000101",
            "101111111111111111110101",
            "101000000000000000010001",
            "100011111111111111011101",
            "111010000000000000010111",
            "100000111111011111110011",
            "101110000000000000110011",
            "101000111111111110000001",
            "111111111111111111111111",
        ]
    ]
    return labyrinthes[niveau - 1]

case_size = 50

def dessiner_labyrinthe(lab):
    for y, ligne in enumerate(lab):
        for x, case in enumerate(ligne):
            if case == "1":
                screen.blit(pygame.transform.scale(sprite_mur, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "0":
                screen.blit(pygame.transform.scale(sprite_sol, (case_size, case_size)), (x * case_size, y * case_size))

def dessiner_vision():
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    vision_surface.fill((0, 0, 0, 255))
    pygame.draw.circle(vision_surface, (0, 0, 0, 0), (personnage.x + 20, personnage.y + 20), 100)
    screen.blit(vision_surface, (0, 0))

personnage = pygame.Rect(55, 55, 40, 40)
objectif = pygame.Rect(1050, 550, 50, 50)
objectif_color = (0, 0, 0)

vitesse = 50
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))
    screen.blit(play_button_menu, play_button_rect)
    screen.blit(quit_button_image, quit_button_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game_running = True
                running = False
            if quit_button_rect.collidepoint(event.pos):
                running = False

while game_running:
    screen.fill((0, 0, 0))
    labyrinthe = charger_labyrinthe(niveau)
    dessiner_labyrinthe(labyrinthe)
    pygame.draw.rect(screen, objectif_color, objectif)
    screen.blit(personnage_image, (personnage.x, personnage.y))
    dessiner_vision()

    keys = pygame.key.get_pressed()
    new_x, new_y = personnage.x, personnage.y
    if keys[pygame.K_LEFT]:
        new_x -= vitesse
    if keys[pygame.K_RIGHT]:
        new_x += vitesse
    if keys[pygame.K_UP]:
        new_y -= vitesse
    if keys[pygame.K_DOWN]:
        new_y += vitesse

    if labyrinthe[new_y // case_size][new_x // case_size] == "0":
        personnage.x, personnage.y = new_x, new_y

    if personnage.colliderect(objectif):
        victoire = True
        game_running = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    clock.tick(10)

while victoire:
    screen.blit(ecran_victoire, (0, 0))
    screen.blit(bouton_suivant_image, bouton_suivant_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            victoire = False
            game_running = False  # Assurer que le jeu s'arrête
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_suivant_rect.collidepoint(event.pos):
                victoire = False  # Quitter l'écran de victoire
                niveau += 1  # Passer au niveau suivant

                if niveau > 2:  # Si on a fini tous les niveaux, on termine le jeu
                    game_running = False
                else:
                    personnage.x, personnage.y = 55, 55  # Réinitialiser la position
                    objectif = pygame.Rect(1050, 550, 50, 50)  # Assurer que l'objectif est bien positionné
                    game_running = True  # Reprendre le jeu

while game_running:
    screen.fill((0, 0, 0))
    labyrinthe = charger_labyrinthe(niveau)  # Charger le bon labyrinthe selon le niveau
    dessiner_labyrinthe(labyrinthe)
    pygame.draw.rect(screen, objectif_color, objectif)
    screen.blit(personnage_image, (personnage.x, personnage.y))
    dessiner_vision()

    keys = pygame.key.get_pressed()
    new_x, new_y = personnage.x, personnage.y
    if keys[pygame.K_LEFT]:
        new_x -= vitesse
    if keys[pygame.K_RIGHT]:
        new_x += vitesse
    if keys[pygame.K_UP]:
        new_y -= vitesse
    if keys[pygame.K_DOWN]:
        new_y += vitesse

    if labyrinthe[new_y // case_size][new_x // case_size] == "0":
        personnage.x, personnage.y = new_x, new_y

    if personnage.colliderect(objectif):
        victoire = True
        game_running = False  # Sortir de la boucle pour aller à l'écran de victoire

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    clock.tick(10)

pygame.quit()
