from pydots import cycle
import random
import json
import pygame


print('starting')

dots = []
i = 0 
while i < 100:
  dots.append([random.randint(2, 254), random.randint(2, 254), 0, 0, 0, 0, random.randint(1, 10)])
  i += 1

j = 0

pygame.init()

surf = pygame.display.set_mode((256, 256))
clock = pygame.time.Clock()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      dots.append([x, y, 0, 0, 0, 0, random.randint(1, 10)])
  surf.fill((0, 0, 0))
  dn = dots
  for c in range(len(dots)):
    v = cycle(dots[c], dots[:c]+dots[c+1:])
    if len(v) == 2:
      dn = dn + v
    else:
      dn[c] = v
  dots = dn
  for d in dots:
    surf.set_at((round(d[0]), round(d[1])), (255, 255, 255))
  pygame.display.flip()
  clock.tick(10000)

print('dumping')
j = json.dumps(dots)
file = open('dump.json', 'w')
print(j)
file.write(j)
file.close()

