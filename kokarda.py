import pygame
from pygame.locals import *
from math import sin, cos, pi, radians
from random import randint

W, H = 1920, 1080
CX, CY = W//2, H//2

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('')

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None, (fs := 60))

colors = [[0,255,0],
          [255,255,255],
          [255,0,0],
          [0,0,255]]

num = 4
mrot = 0

d = True
g = 1

lw = 10
ss = 1

run = True
while run:
   clock.tick(60)
   screen.fill((0,0,0))
   val = pi*2/num

   for j in range(3):
      rad = ss*j
      if rad < CX:
         if g in [1, 3]:
            for i in range(num):
               rot = i*val+radians(mrot)
               dx, dy = cos(rot), sin(rot)
               x, y = dx*(rad+ss)+CX, dy*(rad+ss)+CY
               x2, y2 = dx*rad+CX, dy*rad+CY
               pygame.draw.line(screen, colors[j], (x, y), (x2, y2), int(lw))

         if g in [2, 3]:
         
            for i in range(num):
               posses = [[0,0],[0,0]]
               for p in range(2):
                  rot = (i+p)*val+radians(mrot)
                  dx, dy = cos(rot), sin(rot)
                  posses[p] = [dx*(rad+ss)+CX, dy*(rad+ss)+CY]

               pygame.draw.line(screen, colors[j], posses[0], posses[1], int(lw))
   
   for cn, n in enumerate((data := {
      'n': num, 'lw': lw, 'd': d, 'mode': g, 'rot': f'{mrot%360}'
      })):

      v = data[n]
      s = font.render(f'{n}: {v}', 1, (255,255,255))
      screen.blit(s, (200, fs*cn+110))

   pygame.display.update()

   keys = pygame.key.get_pressed()
   if keys[K_RIGHT]: mrot += 1.5
   if keys[K_LEFT]:  mrot -= 1.5

   if keys[K_l]: lw += 1
   if keys[K_j]: lw -= 1

   if keys[K_e]: ss += 2
   if keys[K_q]: ss -= 2

   if not d:
      if keys[K_UP]: num += 1
      if keys[K_DOWN]: num -= 1

   for e in pygame.event.get():
      if e.type == QUIT:
         run = False

      if e.type == KEYDOWN:
         if d:
            if e.key == K_UP:   num += 1
            if e.key == K_DOWN: num -= 1

         if e.key == K_SPACE: d = not d
         if e.key == K_v: g = [2,3,1][g-1]

         if e.key == K_ESCAPE:
            run = False

         if e.key == K_F11:
            pygame.display.toggle_fullscreen()
   if num < 1: num = 1
   if lw < 1: lw = 1

pygame.image.save(screen, 'lol.png')

pygame.quit()

