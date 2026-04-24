import pygame
pygame.init()
screen = pygame.display.set_mode((1050, 1050))
clock = pygame.time.Clock()
running = True
icon = pygame.image.load('icon.png')
pygame.display.set_caption("GeometrySim")
pygame.display.set_icon(icon)

ox = 525
oy = 525
scale = 49
cols = 1050//scale +2
def drawnums():
    font = pygame.font.SysFont("Arial", 15)
    cols = int((1050 // scale) + 2)
    rows = int((1050 // scale) + 2)

    for i in range(-cols, cols + 1):
        x = ox + i * scale - (6 if i < 0 else 3)
        screen.blit(font.render(f"{i}", True, "#adadad"), (x, oy + 8))

    for i in range(-rows, rows + 1):
        if i != 0:
            y = oy - i * scale - 7
            screen.blit(font.render(f"{i}", True, "#adadad"), (ox + 6, y))

def drawaxis():
    pygame.draw.line(screen, "#535353", (ox, 0), (ox, 1050), 2)
    pygame.draw.line(screen, "#535353", (0, oy), (1050, oy), 2)

def drawgrid():
    left = int(ox // scale) + 2
    right = int((1050 - ox) // scale) + 2
    top = int(oy // scale) + 2
    bottom = int((1050 - oy) // scale) + 2

    for i in range(-left, right + 1):
        x = ox + i * scale
        pygame.draw.line(screen, "#333333", (x, 0), (x, 1050), 1)

    for i in range(-top, bottom + 1):
        y = oy + i * scale
        pygame.draw.line(screen, "#333333", (0, y), (1050, y), 1)

class Line:
    def __init__(self,x1,y1,x2,y2):
       self.x1 = x1
       self.y1 = y1
       self.x2 = x2
       self.y2 = y2
    def draw(self,screen,ox,oy,scale):
        sx1 = ox+self.x1 * scale
        sy1 = oy-self.y1 * scale
        sx2 = ox+self.x2 * scale
        sy2 = oy-self.y2 * scale 
        pygame.draw.line(screen, "white", (sx1, sy1), (sx2, sy2), 2)
class Polygon:
    def __init__(self,points,color="white"):
        self.points = points
        self.color = color

    def draw(self,screen,ox,oy,scale):
        converted = []
        for x, y in self.points:
            sx = ox + x * scale
            sy = oy - y * scale
            converted.append((sx,sy))
        pygame.draw.polygon(screen,self.color,converted,2)
lines = [
    Line(0,0,1,1),
    Polygon([(2,0), (1,2), (-1,2), (-2,0), (-1,-2), (1,-2)])
]

while running:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            scale = max(10,scale+event.y *3)
    screen.fill("black")
    gx = round((mx-ox)/scale)
    gy = round((oy-my)/scale)
    sx = ox + gx * scale
    sy = oy - gy * scale
    pygame.draw.circle(screen,"white",(sx,sy),5)
    drawgrid()
    drawaxis()
    drawnums()
    for line in lines:
        line.draw(screen,ox,oy,scale)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()