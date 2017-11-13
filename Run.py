# Ian Davis jid7da 2d top down portal


import gamebox
import pygame
import math
CAMERA_WIDTH, CAMERA_HEIGHT = 1000, 600
BOX_WIDTH, BOX_HEIGHT = 20, 35
camera = gamebox.Camera(CAMERA_WIDTH, CAMERA_HEIGHT)
playeroneimage = 'Goku-1.png'
playerone = gamebox.from_image(300, 400, playeroneimage)
playerone.scale_by(1.75)
background = gamebox.from_color(500, 600, "green", 700, 50)

def tick(keys):
    global playeroneimage, playerone
    camera.clear("black")

    if pygame.K_UP in keys:
        playerone.yspeed = -10

    if pygame.K_DOWN in keys and playerone.touches(background):
        playerone = gamebox.from_image(playerone.x, background.y-30, 'Goku-crouch.png')
        playerone.scale_by(1.75)
    elif pygame.K_DOWN not in keys and playerone.touches(background):
        playerone = gamebox.from_image(playerone.x, playerone.y, 'Goku-1.png')
        playerone.scale_by(1.75)

    if pygame.K_RIGHT in keys:
        playerone.x += 4

    if pygame.K_LEFT in keys:
        playerone.x += -4

    playerone.yspeed += .5
    playerone.y = playerone.y + playerone.yspeed
    if playerone.touches(background):
        playerone.move_to_stop_overlapping(background)
    camera.draw(background)
    camera.draw(playerone)
    camera.display()



ticks_per_second = 60
gamebox.timer_loop(ticks_per_second, tick)