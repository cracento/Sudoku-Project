import pygame
import time
from sudoku_generator import SudokuGenerator, generate_sudoku

pygame.init()

screen = pygame.display.set_mode((818, 648))
bg = pygame.image.load("images/bg.png").convert()
font = pygame.font.SysFont(None, 36)

running = True

def draw_title():
    # draw background image
    screen.blit(bg, (0, 0))
    
    # create rectangles for each image
    easy = pygame.Rect(60, 500, 150, 70)
    medium = pygame.Rect(265, 500, 150, 70)
    hard = pygame.Rect(470, 500, 150, 70)

    # draw those rectangles
    pygame.draw.rect(screen, "orange", easy)
    pygame.draw.rect(screen, "orange", medium)
    pygame.draw.rect(screen, "orange", hard)

    # create text for each rectangle
    easytext = font.render("Easy", True, "white")
    mediumtext = font.render("Medium", True, "white")
    hardtext = font.render("Hard", True, "white")

    # draw that text
    screen.blit(ddfcs)
    
    
    

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_title()

pygame.quit()