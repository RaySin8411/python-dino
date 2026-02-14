import pygame 
import os 
import random 

pygame.init() 

screen_height = 600 
screen_width = 1100 

screen = pygame.display.set_mode((screen_width, screen_height))

RUNNING = [ 
	pygame.image.load(os.path.join("assets/Dino", "Chrome Dino Run.png")), 
	pygame.image.load(os.path.join("assets/Dino", "Chrome Dino Run 2.png")) 
] 
JUMPING = pygame.image.load(os.path.join("assets/Dino", "Dino Jump.png")) 
DUCKING = [ 
	pygame.image.load(os.path.join("assets/Dino", "Dino Duck.png")), 
	pygame.image.load(os.path.join("assets/Dino", "Dino Duck 2.png")) 
]

class Dinosaur:
    X_pos = 80
    Y_pos = 310
    Y_pos_duck = 340
    set_jump_vel = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.set_jump_vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 20:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
    
    def duck(self):
        self.image = self.duck_img[self.step_index // 10]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos_duck
        self.step_index += 1


    def run(self):
        self.image = self.run_img[self.step_index // 10]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.85
            print(f"y pos: {self.dino_rect.y}, jump vel: {self.jump_vel: .2f}")
        if self.jump_vel < -self.set_jump_vel:
            self.dino_jump = False
            self.jump_vel = self.set_jump_vel
            print("jump stop", self.jump_vel)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


CLOUD = pygame.image.load(os.path.join("assets/Other", "Chrome Dinosaur Cloud.png"))

class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(500, 2000)
        self.y = random.randint(50, 200)
        self.image = CLOUD
        self.width = self.image.get_width()
    
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screen_width + random.randint(500, 1500)
            self.y = random.randint(50, 200)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


BG = pygame.image.load(os.path.join("assets/Other", "Chrome Dinosaur Track.png"))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width
        
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


SMALL_CACTUS = [
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Small Cactus.png")),
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Small Cactus (1).png")),
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Small Cactus (2).png"))
]

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


LARGE_CACTUS = [
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Large Cactus.png")),
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Large Cactus (1).png")),
    pygame.image.load(
        os.path.join("assets/Cactus", "Chrome Dinosaur Large Cactus (2).png")),
]

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


BIRD = [
    pygame.image.load(
        os.path.join("assets/Bird", "Chrome Dinosaur Bird1.png")),
    pygame.image.load(
        os.path.join("assets/Bird", "Chrome Dinosaur Bird2.png")),
]

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 10:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

