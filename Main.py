import pygame
pygame.init()
pygame.mixer.init()

# Chargement de la musique
pygame.mixer.music.load("Musique/Fort Boyard Main Theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Fenêtre du jeu
pygame.display.set_caption("The maze")
screen = pygame.display.set_mode((1200, 700))

# Chargement des images
background = pygame.image.load("Images/Image d'accueil.jpg")
play_button_menu = pygame.transform.scale(pygame.image.load('Images/Bouton Play.PNG'), (300, 300))
quit_button_image = pygame.transform.scale(pygame.image.load('Images/Bouton Quitter.PNG'), (300, 240))

sprite_sol = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur = pygame.image.load("Images/sprite_mur.jpg")

personnage_image = pygame.transform.scale(pygame.image.load("Images/perso_face.png"), (40, 40))
ecran_victoire = pygame.transform.scale(pygame.image.load("Images/thank_you_for_playing.png"), (1200, 700))
bouton_suivant_image = pygame.image.load("Images/Image_prochain_niveau.png")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))
bouton_suivant_rect = bouton_suivant_image.get_rect(center=(600, 600))

# Variables du jeu
case_size = 50
vitesse = 5  # Vitesse du personnage
clock = pygame.time.Clock()

# Définition des labyrinthes
def charger_labyrinthe(niveau):
    labyrinthes = [
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
        ],
        [
            "111111111111111111111111",
            "100000011100000000000001",
            "101111011101111111110101",
            "101000010001000000010001",
            "101010111111111110111101",
            "100010000000000010000101",
            "101111111101111011110101",
            "100000000101000010000001",
            "101110111101011110111101",
            "101000000001000010000101",
            "101111110111011011110101",
            "101000000000000000000001",
            "101111111111111111111101",
            "111111111111111111111111",
        ]
    ]
    return labyrinthes[niveau - 1]

# Dessiner le labyrinthe
def dessiner_labyrinthe(lab):
    for y, ligne in enumerate(lab):
        for x, case in enumerate(ligne):
            if case == "1":
                screen.blit(pygame.transform.scale(sprite_mur, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "0":
                screen.blit(pygame.transform.scale(sprite_sol, (case_size, case_size)), (x * case_size, y * case_size))

# Vision réduite du joueur
def dessiner_vision():
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    vision_surface.fill((0, 0, 0, 180))
    pygame.draw.circle(vision_surface, (0, 0, 0, 0), (personnage.x + 20, personnage.y + 20), 100)
    screen.blit(vision_surface, (0, 0))

# Nouvelle fonction pour vérifier si le personnage peut se déplacer
def peut_deplacer(x, y, lab):
    if lab[y // case_size][x // case_size] == "0":
        return True
    return False

# Nouvelle fonction pour vérifier les collisions avec les murs
def bloquer_collision(x, y, lab):
    x1, y1 = x // case_size, y // case_size
    x2, y2 = (x + personnage.width) // case_size, (y + personnage.height) // case_size
    if lab[y1][x1] == "1" or lab[y1][x2] == "1" or lab[y2][x1] == "1" or lab[y2][x2] == "1":
        return False
    return True

# Boucle principale du menu
running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(play_button_menu, play_button_rect)
    screen.blit(quit_button_image, quit_button_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                running = False  # Sort du menu pour commencer le jeu
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()

# Boucle principale du jeu
niveau = 1
game_running = True

while game_running:
    personnage = pygame.Rect(55, 55, 40, 40)
    objectif = pygame.Rect(1050, 550, 50, 50)

    victoire = False
    while not victoire:
        screen.fill((0, 0, 0))
        labyrinthe = charger_labyrinthe(niveau)
        dessiner_labyrinthe(labyrinthe)
        pygame.draw.rect(screen, (0, 0, 0), objectif)
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

        # Utilisation des nouvelles fonctions pour vérifier les déplacements
        if bloquer_collision(new_x, personnage.y, labyrinthe):
            personnage.x = new_x
        if bloquer_collision(personnage.x, new_y, labyrinthe):
            personnage.y = new_y

        if personnage.colliderect(objectif):
            victoire = True

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

        clock.tick(60)

    victoire_ecran = True
    while victoire_ecran:
        screen.blit(ecran_victoire, (0, 0))
        screen.blit(bouton_suivant_image, bouton_suivant_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and bouton_suivant_rect.collidepoint(event.pos):
                victoire_ecran = False
                niveau += 1
                if niveau > 3:
                    game_running = False  # Termine le jeu après le dernier niveau
