import pygame
import time
from sudoku_generator import SudokuGenerator, generate_sudoku

pygame.init()

global easy, medium, hard
screen = pygame.display.set_mode((812, 740))
bg = pygame.image.load("images/bg.png").convert()
font = pygame.font.SysFont(None, 36)

running = True

def draw_title():
    screen.fill("black")
    # draw background image
    screen.blit(bg, (0, 0))
    
    # create rectangles for each image
    global easy, medium, hard           # This is done so that the running loop can recognize their positions when checking for mouse button events.
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
    screen.blit(easytext, (107, 525))   # Calculated these with (hard.x + (hard.width - hardtext.get_width()) // 2, hard.y + (hard.height - hardtext.get_height()) // 2).
    screen.blit(mediumtext, (294, 525)) # No reason not to hardcode since the window is always the same size to prevent extra calculations.
    screen.blit(hardtext, (516, 525))

    # create and draw Sudoku text at top of screen. also have to create a new font since the font size is immutable after creating.
    bigfont = pygame.font.SysFont(None, 70)
    sudokutext = bigfont.render("Sudoku!", True, "black")
    screen.blit(sudokutext, (240, 120)) # Manually adjusted since the text should be centered on the Sudoku board.
    
    # update display
    pygame.display.flip()

def draw_board(board):
    screen.fill("white")

    width = 812
    height = 648
    width_floor = 812 // 9
    height_floor = 648 // 9

    # draw horizontal lines
    for row in range(10):     
        thickness = 6 if row % 3 == 0 else 2
        pygame.draw.line(screen, "black", (0, row * height_floor), (width, row * height_floor), thickness)

    # draw vertical lines
    for col in range(10):
        thickness = 6 if col % 3 == 0 else 2
        pygame.draw.line(screen, "black", (col * width_floor, 0), (col * width_floor, height), thickness)

    # create text for game
    resettext = font.render("Reset", True, "white")
    restarttext = font.render("Restart", True, "white")
    exittext = font.render("Exit", True, "white")

    # create rectangles for the text
    global reset, restart, exit
    reset = pygame.Rect(126, 660, 150, 70)
    restart = pygame.Rect(331, 660, 150, 70)
    exit = pygame.Rect(536, 660, 150, 70)

    # draw the rectangles first
    pygame.draw.rect(screen, "black", reset)
    pygame.draw.rect(screen, "black", restart)
    pygame.draw.rect(screen, "black", exit)

    # draw that text
    screen.blit(resettext, (166, 682))
    screen.blit(restarttext, (363, 682))
    screen.blit(exittext, (586, 682))

    # draw board numbers
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0: # make sure we skip zeroes

                # create text for each number
                num_text = font.render(str(num), True, "black")

                # calculate position for each number
                text_x = col * width_floor + (width_floor - num_text.get_width()) // 2
                text_y = row * height_floor + (height_floor - num_text.get_height()) // 2

                # draw the number
                screen.blit(num_text, (text_x, text_y))

    
    # update display 
    pygame.display.flip()

draw_title()
status = "title"
while running:
    # basic pygame event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check for mouse clicks on each button
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickposition = event.pos

            # confirm we are on the title screen
            if status == "title":

                # check if click position coincides with each button, then generate the respective board. if click is somewhere else do nothing
                if easy.collidepoint(clickposition):
                    board = generate_sudoku(9, 30)
                    print("easy board generated")
                    print(board)

                elif medium.collidepoint(clickposition):
                    board = generate_sudoku(9, 40)
                    print("medium board generated")
                    print(board)

                elif hard.collidepoint(clickposition):
                    board = generate_sudoku(9, 50)
                    print("hard board generated")
                    print(board)

                if easy.collidepoint(clickposition) or medium.collidepoint(clickposition) or hard.collidepoint(clickposition):
                    draw_board(board)   # draw board on screen
                    status = "in game"  # change status to in game to prevent clicking old buttons
            
            if status == "in game":

                # check if click position coincides with each button, then follow their action. if click is somewhere else do nothing.
                if reset.collidepoint(clickposition):
                    draw_board(board)

                if restart.collidepoint(clickposition):
                    draw_title()
                    status = "title"

                if exit.collidepoint(clickposition):
                    pygame.quit()
                    print("goodbye")
                    exit()
                
pygame.quit()
print("goodbye")