# LOAD IMAGES for game

import pyglet
from pathlib import Path



from field import game_field



batch = pyglet.graphics.Batch()


TILES_DIRECTORY = Path('snake-tiles')


snake_IMG = {}
for path in TILES_DIRECTORY.glob('*.png'):
    snake_IMG[path.stem] = pyglet.image.load(path)


apple_image = pyglet.image.load('images/apple2.png')


logo_image = pyglet.image.load('images/logo2.png')
x = game_field.origin_xy0_menu[0]+20
y = game_field.origin_xy1_menu[1]-110
logo = pyglet.sprite.Sprite(logo_image, x, y, batch=batch)


heart_image = pyglet.image.load('images/heart.png')
x = game_field.origin_xy1_menu[0]-130
y = game_field.origin_xy1_menu[1]-70
heart = pyglet.sprite.Sprite(heart_image, x, y, batch=batch)


metre_image = pyglet.image.load('images/metr.png')
x = game_field.origin_xy1_menu[0]-140
y = game_field.origin_xy1_menu[1]-120
metre = pyglet.sprite.Sprite(metre_image, x, y, batch=batch)
