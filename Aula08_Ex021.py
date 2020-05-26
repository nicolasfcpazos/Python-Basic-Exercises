# FAÇA UM PROGRAMA QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3.


import pygame
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()







