import pygame
from os.path import join
from random import randint, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = load_image("player.png")
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        #cool down section
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.rect.center += self.direction * self.speed * dt

        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        elif self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0


        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center= (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

    def update(self, dt):
        pass

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.created_time = pygame.time.get_ticks()
        self.kill_after = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
    
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.created_time > self.kill_after:
            self.kill()

def load_image(image):
    return pygame.image.load(join('images', image)).convert_alpha()

def collisions():
    global running
    #collision between player and meteor
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if collision_sprites:
        running = False

    #Collision between laser and meteor
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill() 

def display_score():
    current_time = int(pygame.time.get_ticks()/1000)
    text_surface = font.render(str(current_time), True, (240, 240, 240 ))
    text_rect = text_surface.get_frect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surface, text_rect)
    pygame.draw.rect(display_surface, (240, 240, 240),text_rect.inflate(20, 10).move(0, -7), 5, 10)

#general
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooters")
running = True

clock = pygame.time.Clock()

# Surface Imports
star_surf = load_image("star.png")
laser_surf = load_image("laser.png")
meteor_surf = load_image("meteor.png")
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 40)

#Sprite Group
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

for _ in range(20):
    star = Star(all_sprites, star_surf)

player = Player(all_sprites)

# Custom Event -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_surf, (randint(0, WINDOW_WIDTH), randint(-200, -100)), (all_sprites,meteor_sprites))
            
    #Update Game state
    dt = clock.tick(60)/1000 # gives the delta time in seconds
    all_sprites.update(dt)

    #collisions
    collisions()

    #Draw everything
    display_surface.fill("#3a2e3f")
    all_sprites.draw(display_surface)
    display_score()

    #Update the whole display
    pygame.display.update()

pygame.quit()