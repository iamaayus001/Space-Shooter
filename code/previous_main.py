# import pygame
# from os.path import join
# from random import randint
#
# class Player(pygame.sprite.Sprite):
# 	def __init__(self, groups):
# 		super().__init__(groups)
# 		self.image = pygame.image.load(join("..","images","player.png")).convert_alpha()
# 		self.rect =  self.image.get_frect(bottomright=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# 		self.direction = pygame.math.Vector2()
# 		self.speed = 300
#
# 	def update(self, dt):
# 		# print("Update")
# 		keys = pygame.key.get_pressed()
# 		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
# 		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
#
# 		self.rect.center += self.direction * self.speed * dt
# 		self.direction.normalize() if self.direction else self.direction
#
# 		if self.rect.right >= WINDOW_WIDTH:
# 			self.rect.right = WINDOW_WIDTH
# 		elif self.rect.left <= 0:
# 			self.rect.left = 0
#
# 		if self.rect.bottom >= WINDOW_HEIGHT:
# 			self.rect.bottom = WINDOW_HEIGHT
# 		elif self.rect.top <= 0:
# 			self.rect.top = 0
#
# class Star(pygame.sprite.Sprite):
# 	def __init__(self, groups):
# 		super().__init__(groups)
# 		self.image = pygame.image.load(join("..", "images", "star.png")).convert_alpha()
# 		self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
#
# 	def update(self, dt):
# 		pass
#
#
#
# # general
# pygame.init()
# WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
# display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Space Shooter")
# running = True
# clock = pygame.time.Clock()
#
# # plain surface
# surf = pygame.Surface((100, 200))
# surf.fill("orange")
# x = 100
#
#
# #Sprite Groups
# all_sprites = pygame.sprite.Group()
#
# # importing an image
# # player surface
# #USING SPRITE
#
# for _ in range(20):
# 	Star(all_sprites)
# player = Player(all_sprites)
# # all_sprites.add(player)
#
# # path = join('..','images', 'player.png')
# # player_surf = pygame.image.load(path).convert_alpha()
# # player_rect = player_surf.get_frect(bottomright=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# # # player_direction = pygame.math.Vector2(1, 0)
# # player_direction = pygame.math.Vector2()
# # player_speed = 300
#
# # star surface
# # path1 = join('..','images', 'star.png')
# # star_surf = pygame.image.load(path1).convert_alpha()
# # star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
#
#
# # meteor surface
# meteor_surf = pygame.image.load(join('..','images', 'meteor.png')).convert_alpha()
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
#
# # laser surface
# laser_surf = pygame.image.load((join('..','images', 'laser.png'))).convert_alpha()
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))
# laser_direction = pygame.math.Vector2()
#
# while running:
# 	dt = clock.tick() / 1000  # gives us in seconds dt
# 	# print(clock.get_fps())
# 	# print(dt)
#
# 	# event loop
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
#
#
# 	all_sprites.update(dt)
#
# 		#Only single times one is clicked
# 		# if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
# 		# 	# print("KEYDOWN")
# 		# 	print("Yes")
# 		# if event.type == pygame.MOUSEMOTION:
# 		# 	# print(event.pos)
# 		# 	player_rect.center = event.pos
#
#
# 	#input
#
# 	#pygame.mouse
# 	# print(pygame.mouse.get_pos())
# 	# print(pygame.mouse.get_pressed())
# 	# print(pygame.mouse.get_rel()) If mouse is moving and how fast is it moving
#
# 	#pygame.key
# 	#continuous
# 	# print(pygame.key.get_pressed())
# 	# keys = pygame.key.get_pressed()
# 	# # if keys[pygame.K_1]:
# 	# # 	print(1)
# 	#
# 	# #this is overkill we can simply use
# 	# # if keys[pygame.K_RIGHT]:
# 	# # 	player_direction.x = 1
# 	# # else:
# 	# # 	player_direction.x = 0
# 	#
# 	# player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
# 	# player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
# 	#
# 	# # print((player_direction*player_speed).magnitude())
# 	# player_direction = player_direction.normalize() if player_direction else player_direction
# 	# player_rect.center += player_direction * player_speed * dt
#
# 	keys_just_pressed = pygame.key.get_just_pressed()
#
# 	#laser_input
# 	# if keys_just_pressed[pygame.K_SPACE]:
# 	# 	print("Fire Laser")
#
#
# 	# draw the game
# 	# background
# 	display_surface.fill("darkgrey")
#
# 	# # stars
# 	# for pos in star_positions:
# 	# 	display_surface.blit(star_surf, pos)
#
# 	# meteor
# 	display_surface.blit(meteor_surf, meteor_rect)
#
# 	# laser
# 	display_surface.blit(laser_surf, laser_rect)
#
# 	# player
# 	# x+=0.1
# 	# player_rect.x += 20
# 	# player_rect.y -= 10
# 	# if player_rect.bottom >= WINDOW_HEIGHT:
# 	#     player_rect.bottom = WINDOW_HEIGHT
# 	#     player_rect.y = -1
# 	# if player_rect.bottom >= WINDOW_HEIGHT:
# 	# 	player_rect.bottom = WINDOW_HEIGHT
# 	# 	player_direction.y *= -1
# 	# elif player_rect.top <= 0:
# 	# 	player_rect.top = 0
# 	# 	player_direction.y *= -1
# 	#
# 	# if player_rect.right >= WINDOW_WIDTH:
# 	# 	player_rect.right = WINDOW_WIDTH
# 	# 	player_direction.x *= -1
# 	# elif player_rect.left <= 0:
# 	# 	player_rect.left = 0
# 	# 	player_direction.x *= -1
#
# 	# player_rect.x += player_direction * 0.4
# 	# if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
# 	#     player_direction *= -1
#
# 	# creating a plain rect
# 	# plain_rect = pygame.FRect((100, 200))
#
# 	# display_surface.blit(player.image, player.rect)
#
# 	all_sprites.draw(display_surface)
# 	# pygame.display.update()
# pygame.quit()
#
