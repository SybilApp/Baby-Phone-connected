#!/usr/bin/env python3

import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("/media/pi/6CBE-C604/breh.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    time.sleep(5)
    pygame.mixer.music.fadeout(5000)
#   pygame.mixer.music.stop()
    continue
