import pygame
import os

base_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_path)

pygame.init()
pygame.mixer.init()

# Fenêtre du jeu
pygame.display.set_caption("THE MAZE")
screen = pygame.display.set_mode((1200, 800),pygame.RESIZABLE )

#Chargement effet sonore
effet_clef = pygame.mixer.Sound('Musiques/effet_sonore_clef.wav')

# Chargement des images
background = pygame.image.load("Images/background.png")
background_2 = pygame.image.load("Images/background_2.png")
play_button_menu = pygame.transform.scale(pygame.image.load('Images/start.PNG'), (250, 100))
quit_button_menu = pygame.transform.scale(pygame.image.load('Images/exit.PNG'), (250, 100))
levels_button_menu = pygame.transform.scale(pygame.image.load('Images/levels.PNG'), (250, 100))

sprite_sol_1 = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur_1 = pygame.image.load("Images/sprite_mur.jpg")
sprite_sol_2 = pygame.image.load("Images/sprite_sol_2.jpg")
sprite_mur_2 = pygame.image.load("Images/sprite_mur_2.jpg")
sprite_sol_3 = pygame.image.load("Images/sprite_sol_3.jpg")
sprite_mur_3 = pygame.image.load("Images/sprite_mur_3.jpg")
sprite_sol_4 = pygame.image.load("Images/sprite_sol_4.png")
sprite_mur_4 = pygame.image.load("Images/sprite_mur_4.jpg")
sprite_sol_5 = pygame.image.load("Images/sprite_sol_5.png")
sprite_mur_5 = pygame.image.load("Images/sprite_mur_5.png")

sprite_porte = pygame.transform.scale(pygame.image.load("Images/sprite_porte.png"), (50, 50))
sprite_clef = pygame.transform.scale(pygame.image.load("Images/sprite_clef.png"), (50, 50))

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

#Chargement des images des boutons
play_button_rect = play_button_menu.get_rect(center=(260, 160))
levels_button_rect = levels_button_menu.get_rect(center=(260, 300))
quit_button_rect = quit_button_menu.get_rect(center=(260, 440))


niveau1_button_image = pygame.transform.scale(pygame.image.load('Images/level1.png'), (250, 100))
niveau2_button_image = pygame.transform.scale(pygame.image.load('Images/level2.png'), (250, 100))
niveau3_button_image = pygame.transform.scale(pygame.image.load('Images/level3.png'), (250, 100))
niveau4_button_image = pygame.transform.scale(pygame.image.load('Images/level4.png'), (250, 100))
niveau5_button_image = pygame.transform.scale(pygame.image.load('Images/level5.png'), (250, 100))
retour_menu_button_image = pygame.transform.scale(pygame.image.load('Images/retour_menu.png'), (250, 100))

niveau1_button_rect = niveau1_button_image.get_rect(center=(575, 300))
niveau2_button_rect = niveau2_button_image.get_rect(center=(575, 400))
niveau3_button_rect = niveau3_button_image.get_rect(center=(575, 500))
niveau4_button_rect = niveau4_button_image.get_rect(center=(575, 600))
niveau5_button_rect = niveau5_button_image.get_rect(center=(575, 700))
retour_menu_button_rect = retour_menu_button_image.get_rect(center=(200, 700))

# Variables du jeu
case_size = 50
vitesse = 10  # Vitesse du personnage
clock = pygame.time.Clock()

# Définition des labyrinthes
def charger_labyrinthe(niveau):
    labyrinthes = [
                                       [
            #LABYRINTH 1
            "111111111111111111111111",
            "100000000010000000000001",
            "101111111010111110111101",
            "101000100010000000000001",
            "101010101011011111101131",
            "100010001001010100000111",
            "101111111101010111110001",
            "101000000100010100011101",
            "100011110110110101010001",
            "111010000100100001010111",
            "100000111101101111010011",
            "101110110000001011011011",
            "101000000111111000001011",
            "111110111111111111111011",
            "100000000010000000000021",
            "111111111111111111111111",
        ],
        [
            #LABYRINTH 2
            "111111111111111111111111",
            "100011100011000001000001",
            "101000001000011100011101",
            "101111100011000101110101",
            "100000111000010001100001",
            "101110000011111011001111",
            "100010111000110001100011",
            "111010001010030100111011",
            "100011101010110110110001",
            "101000100010100100100111",
            "101111101010001101101111",
            "100110001111011001001011",
            "110000100011001011100011",
            "111101111111101111111111",
            "100000001000020000000001",
            "111111111111111111111111",
        ],
        [
            #LABYRINTH 3
            "111111111111111111111111",
            "100000011000001000000001",
            "101111011011101101110101",
            "101000010001000000010001",
            "101010110111110110111111",
            "100010000000010010000101",
            "111111101101011011110101",
            "101000001101000010000001",
            "100010111001101110111101",
            "101000010011000010000101",
            "101111000110011011110111",
            "101000011110110001010001",
            "101101110000100100011131",
            "111111110111111111111111",
            "120000000000000100000001",
            "111111111111111111111111"
        ],
        [
            #LABYRINTH 4
            "111111111111111111111111",
            "100000001000000001100001",
            "101111111011111101121101",
            "101000100010000000111101",
            "100010101011011111110001",
            "101110001001010100000111",
            "100011111101010111110001",
            "101000000100010100011101",
            "111111110110110101010101",
            "100001000100100001010101",
            "111100011101101111000101",
            "101110110000031011010101",
            "100000000111111000010001",
            "111011111111111101111111",
            "100000000000000000000001",
            "111111111111111111111111",
        ],
        [
            #LABYRINTH 5
            "111111111111111111111111",
            "100000001000000001100001",
            "101111111011111101100101",
            "101000100010000000111101",
            "100010101011011110110001",
            "101110001001000100000111",
            "100011111101010111110001",
            "101000000100010100011101",
            "111111110110110101010101",
            "110001000100100001010111",
            "111100011101101111010011",
            "100110110000001011011021",
            "130000000111011000000001",
            "101111111111011111111111",
            "100000000000000000000001",
            "111111111111111111111111",
        ]
    ]
    return labyrinthes[niveau - 1]


# Dessiner les labyrinthes
def dessiner_labyrinthe(lab, niveau):
    portes = []  # Liste pour stocker les coordonnées des portes
    clefs = [] # Liste pour stocker les coordonnées des clefs
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
                elif niveau == 5:
                    screen.blit(pygame.transform.scale(sprite_mur_5, (case_size, case_size)), (x * case_size, y * case_size))

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
                elif niveau == 5:
                    screen.blit(pygame.transform.scale(sprite_sol_5, (case_size, case_size)), (x * case_size, y * case_size))

            elif case == "2":
                # Dessiner la porte sur le sol
                porte_rect = sprite_porte.get_rect(topleft=(x * case_size, y * case_size))

                # D'abord, dessiner le sol sous la porte
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_sol_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_sol_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_sol_3, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 4:
                    screen.blit(pygame.transform.scale(sprite_sol_4, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 5:
                    screen.blit(pygame.transform.scale(sprite_sol_5, (case_size, case_size)), (x * case_size, y * case_size))

                # Ensuite, dessiner la porte
                screen.blit(sprite_porte, (x * case_size, y * case_size))
                portes.append(porte_rect)


            elif case == "3":
                # Dessiner la clef sur le sol
                clef_rect = sprite_clef.get_rect(topleft=(x * case_size, y * case_size))

                # D'abord, dessiner la clef sous la porte
                if niveau == 1:
                    screen.blit(pygame.transform.scale(sprite_sol_1, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 2:
                    screen.blit(pygame.transform.scale(sprite_sol_2, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 3:
                    screen.blit(pygame.transform.scale(sprite_sol_3, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 4:
                    screen.blit(pygame.transform.scale(sprite_sol_4, (case_size, case_size)), (x * case_size, y * case_size))
                elif niveau == 5:
                    screen.blit(pygame.transform.scale(sprite_sol_5, (case_size, case_size)), (x * case_size, y * case_size))

                # Ensuite, dessiner la porte
                screen.blit(sprite_clef, (x * case_size, y * case_size))
                clefs.append(clef_rect)

    return portes, clefs



# Fonction pour vérifier si le personnage peut se déplacer
def peut_deplacer(x, y, lab, largeur, hauteur):
    """
    Vérifie si le personnage peut se déplacer à la position donnée.
    """
    # Convertir les coordonnées du personnage en coordonnées de grille
    case_x1 = x // case_size
    case_y1 = y // case_size
    case_x2 = (x + largeur - 1) // case_size
    case_y2 = (y + hauteur - 1) // case_size

    # Vérifier les 4 coins du personnage pour éviter les traversées
    if 0 <= case_y1 < len(lab) and 0 <= case_x1 < len(lab[0]):
        if lab[case_y1][case_x1] == "1":
            return False
    if 0 <= case_y1 < len(lab) and 0 <= case_x2 < len(lab[0]):
        if lab[case_y1][case_x2] == "1":
            return False
    if 0 <= case_y2 < len(lab) and 0 <= case_x1 < len(lab[0]):
        if lab[case_y2][case_x1] == "1":
            return False
    if 0 <= case_y2 < len(lab) and 0 <= case_x2 < len(lab[0]):
        if lab[case_y2][case_x2] == "1":
            return False

    return True
def bloquer_collision(new_x, new_y, lab, personnage):
    case_x = new_x // case_size
    case_y = new_y // case_size

    # Vérifier si la position est dans les limites du labyrinthe
    if 0 <= case_y < len(lab) and 0 <= case_x < len(lab[0]):
        if lab[case_y][case_x] == "1":  # Si c'est un mur
            return True

    # Vérifier si le personnage dépasse le bord droit ou bas de l'écran
    if new_x + personnage.width > screen.get_width():  # Collision à droite
        return True
    if new_y + personnage.height > screen.get_height():  # Collision en bas
        return True
    if new_x < 0:  # Collision à gauche
        return True
    if new_y < 0:  # Collision en haut
        return True

    return False


# Menu principal
def menu():
    pygame.mixer.music.load('Musiques/musique_menu.mp3')
    pygame.mixer.music.play(-1)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(play_button_menu, play_button_rect)
        screen.blit(quit_button_menu, quit_button_rect)
        screen.blit(levels_button_menu, levels_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    niveau = 1
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                if levels_button_rect.collidepoint(event.pos):
                    choisir_niveau()

                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        pygame.display.update()

# Choisir le niveau
def choisir_niveau():
    pygame.mixer.music.load('Musiques/musique_menu.mp3')
    pygame.mixer.music.play(-1)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background_2, (0, 0))
        screen.blit(niveau1_button_image, niveau1_button_rect)
        screen.blit(niveau2_button_image, niveau2_button_rect)
        screen.blit(niveau3_button_image, niveau3_button_rect)
        screen.blit(niveau4_button_image, niveau4_button_rect)
        screen.blit(niveau5_button_image, niveau5_button_rect)
        screen.blit(retour_menu_button_image, retour_menu_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if niveau1_button_rect.collidepoint(event.pos):
                    niveau = 1
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                elif niveau2_button_rect.collidepoint(event.pos):
                    niveau = 2
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                elif niveau3_button_rect.collidepoint(event.pos):
                    niveau = 3
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                elif niveau4_button_rect.collidepoint(event.pos):
                    niveau = 4
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                elif niveau5_button_rect.collidepoint(event.pos):
                    niveau = 5
                    lab = charger_labyrinthe(niveau)
                    pygame.mixer.music.stop()
                    play_game(niveau, lab)

                elif retour_menu_button_rect.collidepoint(event.pos):
                    menu()


        pygame.display.update()

# Fonction pour dessiner la vision autour du joueur
def dessiner_vision(personnage):
    vision_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    vision_surface.fill((0, 0, 0, 255))  # Remplir l'écran de noir avec transparence
    pygame.draw.circle(vision_surface, (0, 0, 0, 0), (personnage.x + 20, personnage.y + 20), 100)  # Créer un cercle transparent autour du personnage
    screen.blit(vision_surface, (0, 0))  # Appliquer la surface de vision à l'écran

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
clefs_prises = 0
vitesse = 10  # vitesse du personnage

def play_game(niveau, lab):
    global perso_anim, clefs_prises
    personnage = pygame.Rect(55, 55, 40, 40)  # Position de départ du personnage
    portes, clefs = dessiner_labyrinthe(lab, niveau)  # Dessiner le labyrinthe et obtenir les portes
    clefs_prises = []

    # Lancer la musique selon le niveau
    if niveau == 1:
        pygame.mixer.music.load('Musiques/musique_level_1.mp3')
    elif niveau == 2:
        pygame.mixer.music.load('Musiques/musique_level_2.mp3')
    elif niveau == 3:
        pygame.mixer.music.load('Musiques/musique_level_3.mp3')
    elif niveau == 4:
        pygame.mixer.music.load('Musiques/musique_level_4.mp3')
    elif niveau == 5:
        pygame.mixer.music.load('Musiques/musique_level_5.mp3')
    pygame.mixer.music.play(-1)  

    # Boucle du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        # Charger les touches et définir la direction
        keys = pygame.key.get_pressed()
        new_x, new_y = personnage.x, personnage.y
        personnage_image = perso_images["bas"][0]  # Image par défaut (face vers le bas)

        # Choisir l'image et la direction en fonction de la touche pressée
        if keys[pygame.K_LEFT]:
            new_x -= vitesse
            if peut_deplacer(new_x, personnage.y, lab, personnage.width, personnage.height):  # Vérifier collision gauche
                personnage_image = perso_images["gauche"][perso_anim % len(perso_images["gauche"])]  # Animation gauche
            else:
                new_x = personnage.x  # Annuler déplacement si collision

        if keys[pygame.K_RIGHT]:
            new_x += vitesse
            if peut_deplacer(new_x, personnage.y, lab, personnage.width, personnage.height):  # Vérifier collision droite
                personnage_image = perso_images["droite"][perso_anim % len(perso_images["droite"])]  # Animation droite
            else:
                new_x = personnage.x  # Annuler déplacement si collision

        if keys[pygame.K_UP]:
            new_y -= vitesse
            if peut_deplacer(personnage.x, new_y, lab, personnage.width, personnage.height):  # Vérifier collision haut
                personnage_image = perso_images["haut"][perso_anim % len(perso_images["haut"])]  # Animation haut
            else:
                new_y = personnage.y  # Annuler déplacement si collision

        if keys[pygame.K_DOWN]:
            new_y += vitesse
            if peut_deplacer(personnage.x, new_y, lab, personnage.width, personnage.height):  # Vérifier collision bas
                personnage_image = perso_images["bas"][perso_anim % len(perso_images["bas"])]  # Animation bas
            else:
                new_y = personnage.y  # Annuler déplacement si collision


        for clef_rect in clefs[:]:
            if personnage.colliderect(clef_rect):
                if clef_rect not in clefs_prises:
                    effet_clef.play()
                    clefs_prises.append(clef_rect)  # On stocke les rectangles, pas les images
                clefs.remove(clef_rect)  # Ajouté : ajouter la clé à la liste des clés prises

        # Vérification de la collision avec la porte
        for porte_rect in portes:
            if personnage.colliderect(porte_rect):
                if len(clefs_prises) > 0:  # Vérifie si au moins une clé a été prise
                    pygame.mixer.music.stop()
                    choisir_niveau()  # Revenir au menu si la porte est atteinte
                    
               
        # Mettre à jour les positions du personnage si pas de collision
        personnage.x = new_x
        personnage.y = new_y

        # Dessiner le labyrinthe
        dessiner_labyrinthe(lab, niveau)
        screen.blit(personnage_image, (personnage.x, personnage.y))  # Dessiner l'image du personnage

        # Dessiner la vision autour du personnage
        dessiner_vision(personnage)

        for i in range(len(clefs_prises)):
            x = screen.get_width() - 50 * (i + 1)
            screen.blit(sprite_clef, (x, 10))

        # Animation continue : faire avancer l'index des images
        perso_anim += 1


        # Mettre à jour l'écran
        pygame.display.flip()

        # Gérer la sortie et les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        clock.tick(30)  # Limiter la vitesse de l'animation

menu()

