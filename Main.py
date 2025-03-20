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

sprite_sol_1 = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur_1 = pygame.image.load("Images/sprite_mur.jpg")
sprite_sol_2 = pygame.image.load("Images/sprite_sol_2.jpg")
sprite_mur_2 = pygame.image.load("Images/sprite_mur_2.jpg")
sprite_sol_3 = pygame.image.load("Images/sprite_sol_3.jpg")
sprite_mur_3 = pygame.image.load("Images/sprite_mur_3.jpg")
sprite_sol_4 = pygame.image.load("Images/sprite_sol_4.jpg.png")
sprite_mur_4 = pygame.image.load("Images/sprite_mur_4.jpg")
sprite_porte = pygame.transform.scale(pygame.image.load("Images/sprite_porte.png"), (50, 50))

# Chargement des images du personnage pour les animations
perso_face = [pygame.transform.scale(pygame.image.load(f"Images/perso_face.png"), (40, 40)) for i in range(1, 4)]
perso_face_marche = [pygame.transform.scale(pygame.image.load(f"Images/perso_face_marche.png"), (40, 40)) for i in range(1, 4)]
perso_face_marche2 = [pygame.transform.scale(pygame.image.load(f"Images/perso_face_marche2.png"), (40, 40)) for i in range(1, 4)]

perso_dos = [pygame.transform.scale(pygame.image.load(f"Images/perso_dos.png"), (40, 40)) for i in range(1, 4)]
perso_dos_marche = [pygame.transform.scale(pygame.image.load(f"Images/perso_dos_marche.png"), (40, 40)) for i in range(1, 4)]
perso_dos_marche2 = [pygame.transform.scale(pygame.image.load(f"Images/perso_dos_marche2.png"), (40, 40)) for i in range(1, 4)]

perso_profil_droit = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_droit.png"), (40, 40)) for i in range(1, 4)]
perso_profil_droit_marche = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_droit_marche.png"), (40, 40)) for i in range(1, 4)]
perso_profil_droit_marche2 = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_droit_marche2.png"), (40, 40)) for i in range(1, 4)]

perso_profil_gauche = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_gauche.png"), (40, 40)) for i in range(1, 4)]
perso_profil_gauche_marche = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_gauche_marche.png"), (40, 40)) for i in range(1, 4)]
perso_profil_gauche_marche2 = [pygame.transform.scale(pygame.image.load(f"Images/perso_profil_gauche_marche2.png"), (40, 40)) for i in range(1, 4)]

personnage_image = pygame.transform.scale(pygame.image.load("Images/perso_face.png"), (40, 40))
ecran_victoire = pygame.transform.scale(pygame.image.load("Images/thank_you_for_playing.png"), (1200, 700))
bouton_suivant_image = pygame.image.load("Images/Image_prochain_niveau.png")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))
bouton_suivant_rect = bouton_suivant_image.get_rect(center=(600, 600))

# Variables du jeu
case_size = 50
vitesse = 10  # Vitesse du personnage
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
            "100011100011000001000001",
            "101000001000011100011101",
            "101111100011000101110101",
            "100000111000010001100001",
            "101110000011111011001111",
            "100010111000110001100011",
            "111010001010000100111011",
            "100011101010110110110001",
            "101000100010100100100111",
            "101111101010001101101111",
            "100110001111011001001011",
            "110000100011001011100011",
            "111111111111111111111111",
        ],
        [
            "111111111111111111111111",
            "100000011000001000000001",
            "101111011011101101110101",
            "101000010001000000010001",
            "101010110111110110111111",
            "100010000000010010000101",
            "111111101101001011110101",
            "101000001101101010000001",
            "100010111001000010111101",
            "101000010011011010000101",
            "101111000110000011110111",
            "101000011100111000010011",
            "101011111111111111111111",
            "111111111111111111111111",
        ],
        [
            "111111111111111111111111",
            "100000001000000001100001",
            "101111111011111101100101",
            "101000100010000000111101",
            "100010101011011111110001",
            "101110001001010100000111",
            "100011111101010111110001",
            "101000000100010100011101",
            "111111110110110101010101",
            "110001000100100001010111",
            "111100011101101111010011",
            "100110110000001011011001",
            "100000000111111000000001",
            "111111111111111111111111",
        ]
    ]
    return labyrinthes[niveau - 1]

# Dessiner le labyrinthe
def dessiner_labyrinthe(lab, niveau):
    portes = []  # Liste pour stocker les coordonnées des portes
    for y, ligne in enumerate(lab):
        for x, case in enumerate(ligne):
            if case == "1":
                # Dessiner les murs
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_mur_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_mur_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_mur_3, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 4:
                    screen.blit(pygame.transform.scale(sprite_mur_4, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "0":
                # Dessiner le sol
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_sol_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_sol_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_sol_3, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 4:
                    screen.blit(pygame.transform.scale(sprite_sol_4, (case_size, case_size)), (x * case_size, y * case_size))
            elif case == "2":
                # Dessiner la porte
                porte_rect = sprite_porte.get_rect(topleft=(x * case_size, y * case_size))
                screen.blit(sprite_porte, (x * case_size, y * case_size))
                portes.append(porte_rect) 
    return portes 

# Vision réduite du joueur
def dessiner_vision():
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    vision_surface.fill((0, 0, 0, 255))
    pygame.draw.circle(vision_surface, (0, 0, 0, 0), (personnage.x + 20, personnage.y + 20), 100)
    screen.blit(vision_surface, (0, 0))

# Fonction pour vérifier si le personnage peut se déplacer
def peut_deplacer(x, y, lab):
    if lab[y // case_size][x // case_size] == "0":
        return True
    return False

# Fonction pour vérifier les collisions avec les murs
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

# Liste complète des images d'animation
perso_images = {
    "gauche": [perso_profil_gauche[0], perso_profil_gauche_marche[0], perso_profil_gauche_marche2[0],
               perso_profil_gauche[1], perso_profil_gauche_marche[1], perso_profil_gauche_marche2[1],
               perso_profil_gauche[2], perso_profil_gauche_marche[2], perso_profil_gauche_marche2[2]],

    "droite": [perso_profil_droit[0], perso_profil_droit_marche[0], perso_profil_droit_marche2[0],
               perso_profil_droit[1], perso_profil_droit_marche[1], perso_profil_droit_marche2[1],
               perso_profil_droit[2], perso_profil_droit_marche[2], perso_profil_droit_marche2[2]],

    "haut": [perso_dos[0], perso_dos_marche[0], perso_dos_marche2[0],
             perso_dos[1], perso_dos_marche[1], perso_dos_marche2[1],
             perso_dos[2], perso_dos_marche[2], perso_dos_marche2[2]],

    "bas": [perso_face[0], perso_face_marche[0], perso_face_marche2[0],
            perso_face[1], perso_face_marche[1], perso_face_marche2[1],
            perso_face[2], perso_face_marche[2], perso_face_marche2[2]]
}

# Initialisation de l'index d'animation
perso_anim = 0

while game_running:
    personnage = pygame.Rect(55, 55, 40, 40)

    victoire = False
    while not victoire:
        screen.fill((0, 0, 0))
        labyrinthe = charger_labyrinthe(niveau)
        portes = dessiner_labyrinthe(labyrinthe, niveau)  # Récupérer la liste des portes

        keys = pygame.key.get_pressed()
        new_x, new_y = personnage.x, personnage.y
        personnage_image = perso_face[0]  # Image par défaut si aucune direction n'est enfoncée

        # Si une touche est pressée, choisir l'image correspondante et se déplacer
        if keys[pygame.K_LEFT]:
            new_x -= vitesse
            personnage_image = perso_images["gauche"][perso_anim % len(perso_images["gauche"])]  # Animation gauche
        if keys[pygame.K_RIGHT]:
            new_x += vitesse
            personnage_image = perso_images["droite"][perso_anim % len(perso_images["droite"])]  # Animation droite
        if keys[pygame.K_UP]:
            new_y -= vitesse
            personnage_image = perso_images["haut"][perso_anim % len(perso_images["haut"])]  # Animation haut
        if keys[pygame.K_DOWN]:
            new_y += vitesse
            personnage_image = perso_images["bas"][perso_anim % len(perso_images["bas"])]  # Animation bas

        # Utilisation des nouvelles fonctions pour vérifier les déplacements
        if bloquer_collision(new_x, personnage.y, labyrinthe):
            personnage.x = new_x
        if bloquer_collision(personnage.x, new_y, labyrinthe):
            personnage.y = new_y

        # Vérification de la collision avec la porte
        for porte_rect in portes:
            if personnage.colliderect(porte_rect):
                victoire = True

        screen.blit(personnage_image, (personnage.x, personnage.y))
        dessiner_vision()

        # Animation continue : faire avancer l'index des images
        perso_anim += 1

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

        clock.tick(20)  # Limiter la vitesse de l'animation

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
                if niveau > 4:  # Maintenant, le jeu se termine après le niveau 4
                    game_running = False  # Termine le jeu après le niveau 4
