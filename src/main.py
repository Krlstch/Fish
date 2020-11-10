import math
import os
import pathlib

import pygame
import time

from src.obserer import Observer


def draw(game_display, observer):
    game_display.fill((0, 0, 0))
    for element in observer.objects:
        rotated_sprite = pygame.transform.rotate(element.sprite, element.angle * 180 / math.pi)
        if element.flip:
            rotated_sprite = pygame.transform.flip(rotated_sprite, True, False)

        game_display.blit(rotated_sprite, (int(element.x) - element.width / 2, int(element.y) - element.height / 2))
        if element.x + element.width / 2 > observer.width:
            game_display.blit(rotated_sprite, (int(element.x) - observer.width - element.width / 2, int(element.y) - element.height / 2))
        if element.x - element.width / 2 < 0:
            game_display.blit(rotated_sprite, (int(element.x) + observer.width - element.width / 2, int(element.y) - element.height / 2))

    pygame.display.update()


def load_sprites():
    sprites = {}
    for file in os.listdir('..\\sprites'):
        sprites[file.rsplit('.', 1)[0]] = pygame.image.load("..\\sprites\\" + file)
    return sprites


if __name__ == "__main__":
    run = True
    target_fps = 60
    observer = Observer(load_sprites())
    game_display = pygame.display.set_mode((observer.width, observer.height))

    prev_time = time.time()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        observer.update()
        draw(game_display, observer)

        # Handle time
        curr_time = time.time()
        diff = curr_time - prev_time
        delay = max(1.0 / target_fps - diff, 0)
        time.sleep(delay)
        fps = 1.0 / (delay + diff)
        prev_time = curr_time

    pygame.quit()
    quit(0)
