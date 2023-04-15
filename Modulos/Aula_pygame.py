import pygame
pygame.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load("ex01.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()