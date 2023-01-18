# Создайте программу для игры в ""Крестики-нолики"".
import pygame
import random

pygame.init()

def draw_grid(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 100,), (300, 100), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)



SCREEN_SIZE = (300,300)

window = pygame.display.set_mode((SCREEN_SIZE))
screen = pygame.Surface(SCREEN_SIZE)

pygame.display.set_caption("Крестики нолики")
screen.fill((255, 255, 255))

field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "x"
                x,y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"
            draw_tic_tac_toe(screen, field)

    draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()

