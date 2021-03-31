import random
import pygame

pygame.init()

number = 0
rolling = 0
rollspeed = 1000

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                last_number = number
                while True:
                    number = random.randint(1, 6)
                    if last_number == number:
                        print(last_number, number)
                    else:
                        break

        if event.type == pygame.QUIT:
            running = False

    font = pygame.font.SysFont("robotica", 100)
    img = font.render(str(number), True, (0, 0, 0))

    screen.blit(img, (400, 300))
    pygame.display.update()
