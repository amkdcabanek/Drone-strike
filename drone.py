import pygame
import math


class Drone(pygame.sprite.Sprite):

    def __init__(self, screenWidth, screenHeight):
        super().__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.image = pygame.transform.rotozoom(pygame.image.load("grafika/dronisko.png").convert_alpha(), 0, 0.1)
        self.baseImage = self.image
        self.pos = pygame.math.Vector2(screenWidth / 2, screenHeight / 2)
        self.hitboxRect = self.baseImage.get_rect(center=self.pos)
        self.rect = self.hitboxRect.copy()
        self.speed = 0
        self.altitude = 0
        self.throttle = 0
        self.directionX = 0
        self.directionY = 0
        self.velocityX = 0
        self.velocityY = 0

    def turning(self):
        self.mouse_coords = pygame.mouse.get_pos()

        self.x_change_mouse_player = (self.mouse_coords[0] - self.hitboxRect.centerx)
        self.y_change_mouse_player = (self.mouse_coords[1] - self.hitboxRect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.velocityX = math.sin(-self.angle) * self.speed
        self.velocityY = math.cos(-self.angle) * self.speed
        self.image = pygame.transform.rotate(self.baseImage, -self.angle)
        self.rect = self.image.get_rect(center=self.hitboxRect.center)

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.altitude += 1
        if keys[pygame.K_s]:
            if self.altitude > 0:
                self.altitude -= 1
        if keys[pygame.K_LSHIFT]:
            if self.throttle < 100:
                self.throttle += 1
                self.speed += 0.1
        if keys[pygame.K_LCTRL]:
            if self.throttle > 0:
                self.throttle -= 1
                self.speed -= 0.1



    def flight(self):
        self.pos += pygame.math.Vector2(self.velocityX, self.velocityY)
        self.hitboxRect.center = self.pos
        self.rect.center = self.hitboxRect.center

    def update(self):
        self.get_user_input()
        self.constrainMovement()
        self.turning()
        self.flight()


    def constrainMovement(self):
        if self.rect.right > self.screenWidth:
            self.rect.right = self.screenWidth
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > self.screenHeight - 25:
            self.rect.top = self.screenHeight - 25
        if self.rect.bottom < 25:
            self.rect.bottom = 25
