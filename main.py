import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running = True
icon = pygame.image.load('icon.png')
pygame.display.set_caption("Geometry")
pygame.display.set_icon(icon)
ox = 500
oy = 500
scale = 50
def drawaxis():
    pygame.draw.line(screen,"#535353",(500,0),(500,1000),2)
    pygame.draw.line(screen,"#535353",(0,500),(1000,500),2)
def drawgrid():
    for i in range(20):
        pygame.draw.line(screen,"#333333",(i*scale,1000),(i*scale,0),1)
        pygame.draw.line(screen,"#333333",(1000,i*scale),(0,i*scale),1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    drawgrid()
    drawaxis()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()