import pygame
import sys
import random

pygame.init() #intializing pygame module
pygame.mixer.init() #mixer

#background music and sounds
background_music = pygame.mixer.music.load("retro-arcade-game-music-297305.mp3")
pygame.mixer.music.play(-1)
explosion_sound = pygame.mixer.Sound("explosion-312361.mp3")

#screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb Guessing Game")
clock = pygame.time.Clock()

background = pygame.image.load("dog_background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mad_dog = pygame.image.load("mad_dog.png")
mad_dog = pygame.transform.scale(mad_dog, (WIDTH, HEIGHT))

nose_rect = pygame.Rect(445, 100, 115, 73)
mad_mode = False

#images
left_hand_img = pygame.image.load("left_hand_fist.png").convert_alpha() #closed fist
right_hand_img = pygame.image.load("right_hand_fist.png").convert_alpha()

bomb_img = pygame.image.load("bomb_surprise.png").convert_alpha() #bombs
explosion_img = pygame.image.load("explode.png").convert_alpha()

open_L_img = pygame.image.load("open_LEFT.png").convert_alpha() #open palm
open_R_img = pygame.image.load("open_RIGHT.png").convert_alpha()


#scaling images
left_hand_img = pygame.transform.scale(left_hand_img, (240, 240))
right_hand_img = pygame.transform.scale(right_hand_img, (240, 240))
bomb_img = pygame.transform.scale(bomb_img, (150, 150))
open_L_img = pygame.transform.scale(open_L_img, (240, 240))
open_R_img = pygame.transform.scale(open_R_img, (240, 240))
explosion_img = pygame.transform.scale(explosion_img, (150, 150))

#rectangle placement for hands
left_hand_rect = pygame.Rect(80, 200, 240, 240)
right_hand_rect = pygame.Rect(450, 200, 240 ,240)

#score
score = 0
font = pygame.font.Font(None, 50) #font

#game states
bomb_side = random.choice(["left", "right"]) #bomb randomness choice
revealed = False
show_explosion = False
clicked_hand = None
reveal_timer = 0

def draw():
    
    if mad_mode:
        screen.blit(mad_dog, (0,0))
    else:
        screen.blit(background, (0, 0))
    if not revealed: #bomb not revealed
        screen.blit(left_hand_img, left_hand_rect)
        screen.blit(right_hand_img, right_hand_rect)
        return

    if clicked_hand =="left": #revealing open hand after clicking on it
        screen.blit(open_L_img, left_hand_rect)
        screen.blit(right_hand_img, right_hand_rect)
    else:
        screen.blit(left_hand_img, left_hand_rect)
        screen.blit(open_R_img, right_hand_rect)

    if revealed and not show_explosion: #bomb before exploding
        if clicked_hand == "left" and bomb_side == "left":
            screen.blit(bomb_img, bomb_img.get_rect(center=left_hand_rect.center))
        elif clicked_hand == "right" and bomb_side == "right":
            screen.blit(bomb_img, bomb_img.get_rect(center=right_hand_rect.center))
    if show_explosion: #explosion showing after bomb is revealed for 1 second
        if clicked_hand == "left":
            screen.blit(explosion_img, explosion_img.get_rect(center=left_hand_rect.center))
        else:
            screen.blit(explosion_img, explosion_img.get_rect(center=right_hand_rect.center))

running = True

while running: #main loop

    now = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if event.type == pygame.MOUSEBUTTONDOWN and not revealed:
        mx, my = event.pos

        if nose_rect.collidepoint(mx, my):
            mad_mode = True
            
        if left_hand_rect.collidepoint(mx, my): #left hand click
            revealed = True
            clicked_hand = "left"
            reveal_timer = now

        if right_hand_rect.collidepoint(mx, my): #right hand click
            revealed = True
            clicked_hand = "right"
            reveal_timer = now
            
    if revealed and not show_explosion: #revealing bomb
        if now - reveal_timer >= 1000:
            if clicked_hand == bomb_side:
                show_explosion = True
                reveal_timer = now
                explosion_sound.play()
            else:
                score += 1
                bomb_side = random.choice(["left", "right"])
                revealed = False
                show_explosion = False
                clicked_hand = None
                
    if show_explosion: #explosion
        if now - reveal_timer >= 1000:
            game_over_text = font.render("You Blew Up!", True, (200, 50, 50))
            screen.blit(game_over_text, (300, 25))
            pygame.display.flip()
            pygame.time.wait(500)
            running = False

    draw()
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0)) #score
    screen.blit(score_text, (20, 20))

    pygame.display.flip() #updating display

pygame.quit()
sys.exit()
