import pygame
from circleshape import * # ако се наложи ще имапортираме цялата библиотека
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_LEFT]:   # ако нещо се счупи изтрий 
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_RIGHT]:  # ако нещо се счупи изтрий 
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_UP]:     # ако нещо се счупи изтрий 
            self.move(dt)    
        if keys[pygame.K_s]:
            self.move(-dt)    
        elif keys[pygame.K_DOWN]:   # ако нещо се счупи изтрий 
            self.move(-dt)  
        if keys[pygame.K_SPACE]:
            self.shoot()  
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
            
    def shoot(self):
        shot1 = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot2 = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot3 = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        
        shot1.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot2.velocity = pygame.Vector2(1, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot3.velocity = pygame.Vector2(-1, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

