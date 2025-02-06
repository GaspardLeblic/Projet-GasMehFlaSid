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

sprite_sol = pygame.image.load("Images/sprite_sol.jpg")
sprite_mur = pygame.image.load("Images/sprite_mur.jpg")

play_button_rect = play_button_menu.get_rect(center=(260, 160))
quit_button_rect = quit_button_image.get_rect(center=(260, 320))

personnage_image = pygame.image.load("Images/perso_face.png")
personnage_image = pygame.transform.scale(personnage_image, (40, 40))

ecran_victoire = pygame.image.load("Images/thank-you-for-playing-1.png")
ecran_victoire = pygame.transform.scale(ecran_victoire, (1200, 700))

running = True
game_running = False
victoire = False

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

case_size = 50

def dessiner_labyrinthe():
    for y, ligne in enumerate(labyrinthe):
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
    dessiner_labyrinthe()
    pygame.draw.rect(screen, objectif_color, objectif)
    screen.blit(personnage_image, (personnage.x, personnage.y))
    dessiner_vision()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and personnage.x > 0 and labyrinthe[(personnage.y+personnage.height//2) // case_size][(personnage.x+personnage.width//2 - vitesse) // case_size] == "0":
        personnage.x -= vitesse
    if keys[pygame.K_RIGHT] and personnage.x < screen.get_width() - personnage.width and labyrinthe[(personnage.y+personnage.height//2) // case_size][(personnage.x + personnage.width//2 + vitesse) // case_size] == "0":
        personnage.x += vitesse
    if keys[pygame.K_UP] and personnage.y > 0 and labyrinthe[((personnage.y + personnage.height//2) - vitesse) // case_size][(personnage.x+personnage.width//2) // case_size] == "0":
        personnage.y -= vitesse
    if keys[pygame.K_DOWN] and personnage.y < screen.get_height() - personnage.height and labyrinthe[(personnage.y + personnage.height//2 + vitesse) // case_size][(personnage.x+personnage.width//2) // case_size] == "0":
        personnage.y += vitesse

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
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            victoire = False
pygame.quit()
