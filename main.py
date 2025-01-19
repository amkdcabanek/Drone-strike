try:
    from drone import Drone
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

pygame.init()

screenWidth = 1280
screenHeight = 700
UI_SIZE = 50

UI_COLOR = (243, 216, 60)

font = pygame.font.SysFont('arial', 40)
altitudeSurface = font.render("Altitude :", True, UI_COLOR)
throttleSurface = font.render("Throttle :", True, UI_COLOR)


screen = pygame.display.set_mode((screenWidth + UI_SIZE, screenHeight + UI_SIZE*2))
pygame.display.set_caption("Controller")

clock = pygame.time.Clock()

drone = Drone(screenWidth, screenHeight)
droneGroup = pygame.sprite.GroupSingle()
droneGroup.add(drone)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    droneGroup.update()
    screen.fill((0, 0, 0))

    screen.blit(altitudeSurface, (370, 640, 50, 50))
    altUI = font.render(str(drone.altitude), True, UI_COLOR)
    screen.blit(altUI, (570, 640, 50, 50))

    screen.blit(throttleSurface, (70, 640, 50, 50))
    thrUI = font.render(str(drone.throttle), True, UI_COLOR)
    screen.blit(thrUI, (270, 640, 50, 50))

    pygame.draw.rect(screen, UI_COLOR, (10, 10, 1310, 710), 2, 0, 60, 60, 60, 60)

    screen.blit(drone.image, drone.rect)
    pygame.display.update()
    clock.tick(60)
