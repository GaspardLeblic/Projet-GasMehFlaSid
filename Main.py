import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Musique/Fort Boyard Main Theme.mp3")
pygame.mixer.music.set_volume(0.5)  # régle le volume entre 0.0 et 1.0
pygame.mixer.music.play(-1)  # -1 pour jouer la musique en boucle

#génère la fenêtre de notre jeu
pygame.display.set_caption("The maze")
screen = pygame.display.set_mode((1200, 700))

#charger les images
background = pygame.image.load("Images/Image d'accueil.jpg")
fond_ecran_menu = pygame.image.load('Images/Bouton Play.PNG')
play_button_menu = pygame.transform.scale(fond_ecran_menu, (300, 300))
quit_button_image = pygame.image.load('Images/Bouton Quitter.PNG')
quit_button_image = pygame.transform.scale(quit_button_image, (300, 240))

#charger les sprites
sprite_sol = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur = pygame.image.load("Images/sprite_mur.jpg")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))

running = True
game_running = False

#structure du labyrinthe (1 = mur, 0 = sol)
labyrinthe = [
    "111111111111111111111111",
    "100000000000000000000001",
    "101111111011111111111101",
    "101000110010000000000001",
    "101010100111011111101101",
    "100010001111000100000111",
    "101111111111011111110111",
    "101000000100011111110111",
    "100011110111111111110111",
    "111010000100111111110111",
    "100000111101111111110111",
    "101110110001111111110011",
    "101000100111111111110011",
    "111111111111111111111111",
]

#taille des cases du labyrinthe
case_size = 50

#fonction pour dessiner le labyrinthe
def dessiner_labyrinthe():
    for y, ligne in enumerate(labyrinthe):
        for x, case in enumerate(ligne):
            if case == "1":  # Mur
                screen.blit(pygame.transform.scale(sprite_mur, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "0":  # Sol
                screen.blit(pygame.transform.scale(sprite_sol, (case_size, case_size)), (x * case_size, y * case_size))

#initialisation du personnage
personnage = pygame.Rect(55, 55, 40, 40)  # Position initiale et taille
personnage_color = (255, 0, 0)  # Couleur rouge du personnage

# initialisation de l'objectif
objectif = pygame.Rect(1050, 550, 40, 40)  # Position de l'objectif
objectif_color = (0, 255, 0)  # Couleur verte de l'objectif

#vitesse du personnage
vitesse = 50

#créer un objet Clock pour contrôler les FPS
clock = pygame.time.Clock()

#fonction pour créer l'effet d'ombre (zones non visibles)
def dessiner_vision():
    #on dessine une surface de la couleur noire pour faire l'ombre
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    vision_surface.set_alpha(255)  # Pas de transparence, totalement opaque
    vision_surface.fill((0, 0, 0))  # Couleur noire pour l'ombre
    screen.blit(vision_surface, (0, 0))  # Affiche l'ombre par-dessus tout

    # zone de vision : une zone de 3x3 autour du personnage (le personnage étant au centre)
    #on va afficher 3 blocs en horizontal et 3 blocs en vertical autour du personnage
    start_x = max(0, (personnage.x // case_size) - 1)  #début de la vision à gauche
    start_y = max(0, (personnage.y // case_size) - 1)  #Debut de la vision vers le haut

    #afficher la zone de vision autour du personnage (zone carrée de 3x3)
    for y in range(start_y, start_y + 3):  #3 blocs en hauteur
        for x in range(start_x, start_x + 3):  #3 blocs en largeur
            if 0 <= y < len(labyrinthe) and 0 <= x < len(labyrinthe[0]):
                #si c'est un mur
                if labyrinthe[y][x] == "1":
                    screen.blit(pygame.transform.scale(sprite_mur, (case_size, case_size)), (x * case_size, y * case_size))
                #si c'est un sol
                elif labyrinthe[y][x] == "0":
                    screen.blit(pygame.transform.scale(sprite_sol, (case_size, case_size)), (x * case_size, y * case_size))

#boucle principale
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

#boucle jeu
while game_running:
    screen.fill((0, 0, 0))  #efface l'écran
    dessiner_labyrinthe()  #dessine le labyrinthe

    #met l'effet de vision
    dessiner_vision()

    #dessine le personnage et l'objectif
    pygame.draw.rect(screen, personnage_color, personnage)
    pygame.draw.rect(screen, objectif_color, objectif)

    #déplacer le personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and personnage.x > 0 and labyrinthe[(personnage.y+personnage.height//2) // case_size][(personnage.x+personnage.width//2 - vitesse) // case_size] == "0":
        personnage.x -= vitesse
    if keys[pygame.K_RIGHT] and personnage.x < screen.get_width() - personnage.width and labyrinthe[(personnage.y+personnage.height//2) // case_size][(personnage.x + personnage.width//2 + vitesse) // case_size] == "0":
        personnage.x += vitesse
    if keys[pygame.K_UP] and personnage.y > 0 and labyrinthe[((personnage.y + personnage.height//2) - vitesse) // case_size][(personnage.x+personnage.width//2) // case_size] == "0":
        personnage.y -= vitesse
    if keys[pygame.K_DOWN] and personnage.y < screen.get_height() - personnage.height and labyrinthe[(personnage.y + personnage.height//2 + vitesse) // case_size][(personnage.x+personnage.width//2) // case_size] == "0":
        personnage.y += vitesse

    #vérifie si le personnage a atteint l'objectif
    if personnage.colliderect(objectif):
        print("Félicitations, vous avez gagné !")
        game_running = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            print("Fermeture du jeu")

    #fps
    clock.tick(10)

pygame.quit()

