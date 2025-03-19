import pygame
import time

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

sprite_sol_1 = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur_1 = pygame.image.load("Images/sprite_mur.jpg")
sprite_sol_2 = pygame.image.load("Images/sprite_sol_2.jpg")
sprite_mur_2 = pygame.image.load("Images/sprite_mur_2.jpg")
sprite_sol_3 = pygame.image.load("Images/sprite_sol_3.jpg")
sprite_mur_3 = pygame.image.load("Images/sprite_mur_3.jpg")

personnage_image = pygame.image.load("Images/perso_face.png")
personnage_width = personnage_image.get_width()
personnage_height = personnage_image.get_height()

# Découper l'image du personnage en trois parties égales
image_soldat_1 = pygame.transform.scale(personnage_image.subsurface((0, 0, personnage_width // 3, personnage_height)), (40, 40))
image_soldat_2 = pygame.transform.scale(personnage_image.subsurface((personnage_width // 3, 0, personnage_width // 3, personnage_height)), (40, 40))
image_soldat_3 = pygame.transform.scale(personnage_image.subsurface((2 * personnage_width // 3, 0, personnage_width // 3, personnage_height)), (40, 40))

# Liste pour alterner les images du personnage
soldat_images = [image_soldat_1, image_soldat_2, image_soldat_3]
soldat_index = 0
last_time = time.time()

ecran_victoire = pygame.transform.scale(pygame.image.load("Images/thank_you_for_playing.png"), (1200, 700))
bouton_suivant_image = pygame.image.load("Images/Image_prochain_niveau.png")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))
bouton_suivant_rect = bouton_suivant_image.get_rect(center=(600, 600))

# Chargement de l'image de la porte (objectif)
porte_image = pygame.image.load("Images/Image_porte.png")
porte_image = pygame.transform.scale(porte_image, (50, 50))  # Redimensionner l'image de la porte

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
def dessiner_labyrinthe(lab, niveau):
    for y, ligne in enumerate(lab):
        for x, case in enumerate(ligne):
            if case == "1":
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_mur_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_mur_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_mur_3, (case_size, case_size)), (x * case_size, y * case_size))  # Mur niveau 3
            elif case == "0":
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_sol_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_sol_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_sol_3, (case_size, case_size)), (x * case_size, y * case_size))  # Sol niveau 3

# Vision réduite du joueur
def dessiner_vision():
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    vision_surface.fill((0, 0, 0, 255))
    pygame.draw.circle(vision_surface, (0, 0, 0, 0), (personnage.x + 20, personnage.y + 20), 100)
    screen.blit(vision_surface, (0, 0))

# Fonction pour changer l'image du personnage toutes les 0.4 secondes
def alterner_image_personnage():
    global soldat_index, last_time
    if time.time() - last_time >= 0.4:  # 0.4 secondes d'intervalle
        soldat_index = (soldat_index + 1) % 3
        last_time = time.time()

# Nouvelle fonction pour vérifier les collisions avec les murs
def bloquer_collision(x, y, lab):
    x1, y1 = x // case_size, y // case_size
    x2, y2 = (x + personnage_width) // case_size, (y + personnage_height) // case_size
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
        dessiner_labyrinthe
