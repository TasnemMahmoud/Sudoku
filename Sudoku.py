import pygame
import random

pygame.init()
width, height = 540, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 153)
PINK = (255, 182, 193)
GREEN = (0, 255, 0)

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid(board, num, pos):
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True
    
    def fill_board(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(board, num, (i, j)):
                            board[i][j] = num
                            if not fill_board(board):
                                board[i][j] = 0
                            else:
                                return True
                    return False
        return True

    numbers = list(range(1, 10))
    fill_board(board)
    
    for _ in range(random.randint(40, 50)):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        while board[i][j] == 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
        board[i][j] = 0

    return board

def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def draw_grid(win, board):
    win.fill(WHITE)
    
    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(win, BLACK, (0, i * 60), (540, i * 60), thick)
        pygame.draw.line(win, BLACK, (i * 60, 0), (i * 60, 540), thick)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), 1, BLACK)
                win.blit(text, (j * 60 + 20, i * 60 + 15))

def insert_num(win, board, position):
    i, j = position[1] // 60, position[0] // 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 48:  # '0' key
                    board[i][j] = 0
                    return
                if 1 <= event.key - 48 <= 9:
                    num = event.key - 48
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        win.fill(GREEN, (j * 60, i * 60, 60, 60))
                    else:
                        win.fill(RED, (j * 60, i * 60, 60, 60))
                        pygame.display.update()
                    return
        draw_grid(win, board)
        pygame.display.update()

board = generate_board()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            insert_num(win, board, position)
    
    draw_grid(win, board)
    pygame.display.update()

pygame.quit()