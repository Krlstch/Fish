import math

import pygame
from src.player import Player


class Observer:
    def __init__(self, sprites):
        self.height = 800
        self.width = 1000
        self.objects = set()
        self.player = Player(x=self.width / 2, y=self.height / 2, angle=0, width=100, height=50 ,
                             flip=False, observer=self, max_vspeed=1.8, max_hspeed=0.8, friction=0.01, vacceleration=0.2, hacceleration=0.2, sprite=sprites["player"])
        self.objects.add(self.player)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player.send_input("w")
        if keys[pygame.K_s]:
            self.player.send_input("s")
        if keys[pygame.K_a]:
            self.player.send_input("a")
        if keys[pygame.K_d]:
            self.player.send_input("d")

        self.player.update_position()
