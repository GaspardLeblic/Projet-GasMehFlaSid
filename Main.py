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
    "101000001010000000000001",
    "101011100010111111101111",
    "100010001110000100000111",
    "111111111111111111110111",
    "111111111111111111110111",
    "111111111111111111110111",
    "111111111111111111110111",
    "111111111111111111110111",
    "111111111111111111110011",
    "111111111111111111110011",
    "111111111111111111111111",
]

#taille des cases du labyrinthe
case_size = 50

#fonction pour dessiner le labyrinthe
def dessiner_labyrinthe():
    for y, ligne in enumerate(labyrinthe):
        for x, case in enumerate(ligne):
            if case == "1":  #mur
                screen.blit(pygame.transform.scale(sprite_mur, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "0":  #sol
                screen.blit(pygame.transform.scale(sprite_sol, (case_size, case_size)), (x * case_size, y * case_size))

#initialisation du personnage
personnage = pygame.Rect(50, 50, 40, 40)  # Position initiale et taille
personnage_color = (255, 0, 0)  # Couleur rouge du personnage

#initialisation de l'objectif
objectif = pygame.Rect(1050, 550, 40, 40)  # Position de l'objectif
objectif_color = (0, 255, 0)  # Couleur verte de l'objectif

#vitesse du personnage
vitesse = 5

# boucle principale
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

    #dessine le personnage et l'objectif
    pygame.draw.rect(screen, personnage_color, personnage)
    pygame.draw.rect(screen, objectif_color, objectif)

    #déplacer le personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and personnage.x > 0 and labyrinthe[personnage.y // case_size][(personnage.x - vitesse) // case_size] == "0":
        personnage.x -= vitesse
    if keys[pygame.K_RIGHT] and personnage.x < screen.get_width() - personnage.width and labyrinthe[personnage.y // case_size][(personnage.x + personnage.width + vitesse) // case_size] == "0":
        personnage.x += vitesse
    if keys[pygame.K_UP] and personnage.y > 0 and labyrinthe[(personnage.y - vitesse) // case_size][personnage.x // case_size] == "0":
        personnage.y -= vitesse
    if keys[pygame.K_DOWN] and personnage.y < screen.get_height() - personnage.height and labyrinthe[(personnage.y + personnage.height + vitesse) // case_size][personnage.x // case_size] == "0":
        personnage.y += vitesse

    # verifier si le personnage a atteint l'objectif
    if personnage.colliderect(objectif):
        print("Félicitations, vous avez gagné !")
        game_running = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            print("Fermeture du jeu")

pygame.quit()
