# Chargement de la musique
pygame.mixer.music.load("Musique/musique_menu.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
#pygame.mixer.music.load("Musique/musique_niveau_1.mp3")
#pygame.mixer.music.load("Musique/musique_niveau_2.mp3")
#pygame.mixer.music.load("Musique/musique_niveau_3.mp3")
#pygame.mixer.music.load("Musique/musique_niveau_4.mp3")
#pygame.mixer.music.load("Musique/musique_niveau_5.mp3")

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
sprite_sol_5 = pygame.image.load("Images/sprite_sol_5.png")
sprite_mur_5 = pygame.image.load("Images/sprite_mur_5.png")
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

niveau1_button_image = pygame.transform.scale(pygame.image.load('Images/niveau1.png'), (200, 200))
niveau2_button_image = pygame.transform.scale(pygame.image.load('Images/niveau2.png'), (200, 200))
niveau3_button_image = pygame.transform.scale(pygame.image.load('Images/niveau3.png'), (200, 200))
niveau4_button_image = pygame.transform.scale(pygame.image.load('Images/niveau4.png'), (200, 200))
niveau5_button_image = pygame.transform.scale(pygame.image.load('Images/niveau5.png'), (200, 200))

niveau1_button_rect = niveau1_button_image.get_rect(center=(300, 200))
niveau2_button_rect = niveau2_button_image.get_rect(center=(600, 200))
niveau3_button_rect = niveau3_button_image.get_rect(center=(900, 200))
niveau4_button_rect = niveau4_button_image.get_rect(center=(450, 500))
niveau5_button_rect = niveau5_button_image.get_rect(center=(750, 500))

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
            "101110110000001011011211",
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
            "110000100011021011100011",
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
            "101000011100111000010211",
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
            "100110110000001011011021",
            "100000000111111000000001",
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
            "100110110000001011011021",
            "100000000111111000000001",
            "111111111111111111111111",
        ]
    ]
    return labyrinthes[niveau - 1]

# Dessiner le labyrinthe
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

    return portes




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

# Fonction pour retourner au menu après la victoire
def retour_menu():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Musique/Fort Boyard Main Theme.mp3")
    pygame.mixer.music.play(-1)
    return menu()

# Menu principal
def menu():
    continuer = True
    while continuer:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(play_button_menu, play_button_rect)
        screen.blit(quit_button_image, quit_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    choisir_niveau()

                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        pygame.display.update()

# Choisir le niveau
def choisir_niveau():
    continuer = True
    while continuer:
        screen.fill((0, 0, 0))
        screen.blit(niveau1_button_image, niveau1_button_rect)
        screen.blit(niveau2_button_image, niveau2_button_rect)
        screen.blit(niveau3_button_image, niveau3_button_rect)
        screen.blit(niveau4_button_image, niveau4_button_rect)
        screen.blit(niveau5_button_image, niveau5_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if niveau1_button_rect.collidepoint(event.pos):
                    niveau = 1
                    lab = charger_labyrinthe(niveau)
                    play_game(niveau, lab)

                elif niveau2_button_rect.collidepoint(event.pos):
                    niveau = 2
                    lab = charger_labyrinthe(niveau)
                    play_game(niveau, lab)

                elif niveau3_button_rect.collidepoint(event.pos):
                    niveau = 3
                    lab = charger_labyrinthe(niveau)
                    play_game(niveau, lab)

                elif niveau4_button_rect.collidepoint(event.pos):
                    niveau = 4
                    lab = charger_labyrinthe(niveau)
                    play_game(niveau, lab)
                elif niveau5_button_rect.collidepoint(event.pos):
                    niveau = 5
                    lab = charger_labyrinthe(niveau)
                    play_game(niveau, lab)

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
vitesse = 10  # vitesse du personnage

def play_game(niveau, lab):
    global perso_anim
    personnage = pygame.Rect(55, 55, 40, 40)  # Position de départ du personnage
    portes = dessiner_labyrinthe(lab, niveau)  # Dessiner le labyrinthe et obtenir les portes

    # Boucle du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Remplir l'écran avec une couleur de fond
        screen.fill((0, 0, 0))

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

        # Vérification de la collision avec la porte
        for porte_rect in portes:
            if personnage.colliderect(porte_rect):
                retour_menu()  # Revenir au menu si la porte est atteinte

        # Mettre à jour les positions du personnage si pas de collision
        personnage.x = new_x
        personnage.y = new_y

        # Dessiner le labyrinthe
        dessiner_labyrinthe(lab, niveau)
        screen.blit(personnage_image, (personnage.x, personnage.y))  # Dessiner l'image du personnage

        # Dessiner la vision autour du personnage
        dessiner_vision(personnage)

        # Animation continue : faire avancer l'index des images
        perso_anim += 1

        # Mettre à jour l'écran
        pygame.display.flip()

        # Gérer la sortie et les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        clock.tick(20)  # Limiter la vitesse de l'animation


menu()


menu()
