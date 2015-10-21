import sys, pygame
pygame.init()

clock = pygame.time.Clock()

width = 1150
height = 1000
size = width, height

speedx = 12
speedy = 10
speed = [speedx, speedy]

speedx1 = 10
speedy1 = 12
speed1 = [speedx1, speedy1]

speedx2 = 12
speedy2 = 12
speed2 = [speedx2, speedy2]

speedx3 = 10
speedy3 = 10
speed3 = [speedx3, speedy3]

bgColor = r,g,b = 255, 0, 255


screen = pygame.display.set_mode(size)

ball = pygame.image.load("cougar.png")
ballrect = ball.get_rect()

ball1 = pygame.image.load("Keasarge-School-District.png")
ball1rect = ball1.get_rect()

ball2 = pygame.image.load("Keasarge-School-District.png")
ball2rect = ball2.get_rect()

ball3 = pygame.image.load("cougar.png")
ball3rect = ball3.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		bgColor = r,g,b = 255, 180, 0

	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		bgColor = r,g,b = 0, 0, 255

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ball1rect = ball1rect.move(speed1)
	if ball1rect.left < 0 or ball1rect.right > width:
		speed1[0] = -speed1[0]
		bgColor = r,g,b = 255, 180, 0

	if ball1rect.top < 0 or ball1rect.bottom > height:
		speed1[1] = -speed1[1]
		bgColor = r,g,b = 0, 0, 255
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ball2rect = ball2rect.move(speed2)
	if ball2rect.left < 0 or ball2rect.right > width:
		speed2[0] = -speed2[0]

	if ball2rect.top < 0 or ball2rect.bottom > height:
		speed2[1] = -speed2[1]
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ball3rect = ball3rect.move(speed3)
	if ball3rect.left < 0 or ball3rect.right > width:
		speed3[0] = -speed3[0]

	if ball3rect.top < 0 or ball3rect.bottom > height:
		speed3[1] = -speed3[1]

	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(ball, ballrect)
	screen.blit(ball1, ball1rect)
	screen.blit(ball2, ball2rect)
	screen.blit(ball3, ball3rect)
	pygame.display.flip()
	clock.tick(60)


