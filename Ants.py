import pygame
import random as rnd


class Ants(object):
    def __init__(self):
        self._x = 50
        self._y = 50
        self._orient = 0

    def turnL(self):
        self._orient -= 1
        self._orient %= 4

    def turnR(self):
        self._orient += 1
        self._orient %= 4

    def move(self):
        if self._orient == 0:
            self.y -= 1
        elif self._orient == 1:
            self.x += 1
        elif self._orient == 2:
            self.y += 1
        elif self._orient == 3:
            self.x -= 1
        # Corection
        if self._x < 0:
            self._x = 254
        if self._x > 254:
            self._x = 0
        if self._y < 0:
            self._y = 143
        if self._y > 143:
            self._y = 0

    def __get__x(self):
        return self._x

    def __set__x(self, x):
        self._x = x

    def __get__y(self):
        return self._y

    def __set__y(self, y):
        self._y = y

    x = property(__get__x, __set__x)
    y = property(__get__y, __set__y)


ants = []  # Ants array

for i in range(3):  # Change the number of ants here
    ants.append(Ants())
    ants[i].x = rnd.randint(0, 255)  # Random pos for each ants
    ants[i].y = rnd.randint(0, 144)

Grid = [[0] * 144 for _ in range(255)]

# Pygame Init
pygame.init()
screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Langton's Ants")

font = pygame.font.SysFont("arial", 20)
text1 = font.render("Ticks : ", True, (255, 255, 255))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
tick = 0
continuer = 1
screen.fill(BLACK)

# -------- Loop -----------
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    for ant in ants:
        if Grid[ant.x][ant.y] == 0:
            Grid[ant.x][ant.y] = 1
            pygame.draw.rect(screen, WHITE, [5 * ant.x, 5 * ant.y, 5, 5])
            ant.turnL()
            ant.move()

        else:
            Grid[ant.x][ant.y] = 0
            pygame.draw.rect(screen, BLACK, [5 * ant.x, 5 * ant.y, 5, 5])
            ant.turnR()
            ant.move()

    tick += 1

    text2 = font.render(str(tick), True, WHITE)

    pygame.draw.rect(screen, BLACK, [0, 0, 100, 50])

    screen.blit(text1, (10, 5))
    screen.blit(text2, (10, 25))

    pygame.display.flip()

pygame.quit()