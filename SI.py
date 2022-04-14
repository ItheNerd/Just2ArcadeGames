import pygame
import math
import random
import os

# Initialize pygame module
pygame.init()

clock = pygame.time.Clock()
FPS = 30

# Create the screen
display_width, display_height = 800, 545
screen = pygame.display.set_mode((display_width, display_height))
score_value = 0

# Background
background = pygame.image.load(os.path.join("Assets1", "background.jpg"))

# Title and Icon
pygame.display.set_caption("Arcade Game")
icon = pygame.image.load(os.path.join("Assets1", "ufo.png"))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets1", "jet.png")), (80, 80)
)
playerX = 370
playerY = 460
player_change = 0
playerX += player_change


def player(x, y):
    screen.blit(playerImg, (x, y))


# bot
botImg = []
botX = []
botY = []
botX_change = []
botY_change = []
num_of_bots = 6


def bot(x, y, i):
    screen.blit(botImg[i], (x, y))


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)


for i in range(num_of_bots):
    botImg.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("Assets1", "ufo.png")), (67, 67)
        )
    )
    botX.append(random.randint(0, 736))
    botY.append(random.randint(50, 150))
    botX_change.append(2)
    botY_change.append(40)

# Bullet
bulletImg = pygame.image.load(os.path.join("Assets1", "bullet.png"))
bulletX = 500
bulletY = 480
bulletX_change = 500
bulletY_change = 10
bullet_state = "rest"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Score
font = pygame.font.SysFont("Ariel", 40)
textX = 670
textY = 510


def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


# Game Over Text
over_font = pygame.font.SysFont("Ariel", 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (200, 250))


def isCollision(botX, botY, bulletX, bulletY):
    distance = math.sqrt((math.pow(botX - bulletX, 2)) + (math.pow(botY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


# Menu
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.fill(BLACK)
            largeText = pygame.font.Font("freesansbold.ttf", 75)
            TextSurf, TextRect = text_objects("ARCADE GAMES", largeText)
            TextRect.center = ((display_width / 2), 200)
            screen.blit(TextSurf, TextRect)

            button("GAME 1", 100, 400, 150, 45, GREEN, BRIGHT_GREEN, "play1")
            button("GAME 2", 320, 400, 150, 45, GREEN, BRIGHT_GREEN, "play2")
            button("EXIT", 550, 400, 150, 45, RED, BRIGHT_RED, "quit")

            pygame.display.update()
            clock.tick(15)


# Defining Game Loop
def game_loop():
    global playerX
    global playerY
    global player_change
    global bulletX
    global bulletY
    global bulletX_change
    global bulletY_change
    global bullet_state
    global bulletImg
    global score_value
    run = True
    while run:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # If keystroke is pressed check whether its left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change = -5
                if event.key == pygame.K_RIGHT:
                    player_change = 5
                if event.key == pygame.K_LCTRL:
                    if bullet_state == "rest":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_change = 0

        # boundary for spaceship
        playerX += player_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 710:
            playerX = 710

        # bot movement
        for i in range(num_of_bots):

            # Game Over
            if botY[i] > 430:
                for j in range(num_of_bots):
                    botY[j] = 2000
                game_over_text()
                break

            botX[i] += botX_change[i]
            if botX[i] <= 0:
                botX_change[i] = 4
                botY[i] += botY_change[i]
            elif botX[i] >= 736:
                botX_change[i] = -4
                botY[i] += botY_change[i]
            # Collision
            collision = isCollision(botX[i], botY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "rest"
                score_value += 1
                botX[i] = random.randint(0, 736)
                botY[i] = random.randint(50, 150)

            bot(botX[i], botY[i], i)

        # Bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "rest"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()


def button(msg, x, y, w, h, inactivecolour, activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, activecolour, (x, y, w, h))
        if click[0] == 1:
            if action == "play1":
                game_loop()
            if action == "play2":
                import P.py

                P.py.game()
                pygame.quit()
                quit()

            if action == "quit":
                pygame.quit()

    else:
        pygame.draw.rect(screen, inactivecolour, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


game_intro()
