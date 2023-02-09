# CLASS for Game state

import pyglet
from random import randrange


from field import game_field
from images_load import snake_IMG, batch, apple_image


class GameState:
    """
    Game state class. Snake settings, movement settings, Food settings ...
    """
    def __init__(self):
        self.snake_xy = [(0, 0), (0, 1), (0, 2)]
        self.snake_sprites = []
        self.snake_directions = ['tail-top', 'bottom-top', 'bottom-head']
        self.direction = (0, 1)
        self.direction0 = (0, 0)
        self.food_xy = [(3, 3)]
        self.food_sprites = []
        self.draw_food()
        self.food_max = 10
        self.lives = 3
        self.state = 'alive'
        self.keys = []

    def directions(self, head):
        """
        Setting the list with directions of single snake parts.
        It is needed for choice the IMG for snake.
        """
        self.snake_directions = []
        help_list = []
        dict_directions = {(0, 1): 'top', (0, -1): 'bottom', (1, 0): 'right', (-1, 0): 'left'}

        for index, xy in enumerate(self.snake_xy):
            if index == len(self.snake_xy) - 1:
                to_dir = head
            else:
                x_change = self.snake_xy[index+1][0] - xy[0]
                y_change = self.snake_xy[index+1][1] - xy[1]
                to_dir = dict_directions[(x_change, y_change)]
            help_list.append(to_dir)

        for index, item in enumerate(help_list):
            if index == 0:
                from_to_dir = 'tail-' + help_list[index]
            else:
                if help_list[index-1] == 'top':
                    from_dir = 'bottom'
                if help_list[index-1] == 'bottom':
                    from_dir = 'top'
                if help_list[index-1] == 'left':
                    from_dir = 'right'
                if help_list[index-1] == 'right':
                    from_dir = 'left'
                from_to_dir = from_dir + '-' + help_list[index]
            self.snake_directions.append(from_to_dir)

    def draw_snake_parts(self):
        """Draw the right IMG for each part of snake on the right place."""
        self.snake_sprites.clear()
        for index, xy in enumerate(self.snake_xy):
            x = xy[0]*game_field.square_size + game_field.border
            y = xy[1]*game_field.square_size + game_field.border
            img_name = self.snake_directions[index]
            self.snake_sprites.append(pyglet.sprite.Sprite(snake_IMG[img_name], x, y, batch=batch))

    def move(self, t):
        """
        Snake movement in the set direction.
        Also solve these situations:
                --> Snake out of game field
                --> Snake eats itself
                --> Snake eats food
        """
        if self.state == 'alive':
            # Snake head coordinates
            x = self.snake_xy[-1][0] + self.direction[0]
            y = self.snake_xy[-1][1] + self.direction[1]

            # Snake head is out of game field or Snake eats itself
            if x not in range (0, game_field.collums) or y not in range(0, game_field.rows) or (x, y) in self.snake_xy:
                self.directions('dead')
                self.draw_snake_parts()
                self.state = 'dead'
                self.direction0 = self.direction
                self.lives -= 1
                if self.lives == 0:
                    self.state = 'game_over'
                return

            self.snake_xy.append((x, y))

            # Snake eats food
            if (x, y) in self.food_xy:
                food_index = self.food_xy.index((x, y))
                del self.food_sprites[food_index]
                del self.food_xy[food_index]
                self.directions('tongue')

            # Snake only move
            else:
                del self.snake_xy[0]
                del self.snake_sprites[0]
                self.directions('head')
            self.draw_snake_parts()
            self.draw_food()

        if self.state == 'dead' and self.direction0 != self.direction:
            self.state = 'alive'

    def restart_conditions(self):
        self.snake_xy = [(0, 0), (0, 1), (0, 2)]
        self.direction = (0, 1)
        self.direction0 = (0, 0)
        self.food_xy = [(3, 3)]
        self.food_sprites = []
        self.draw_food()
        self.lives = 3
        self.state = 'alive'
        self.keys = []

    def add_food(self, t):
        """Add food in food list."""
        if self.state == 'alive':
            while True:
                x = randrange(0, game_field.collums)
                y = randrange(0, game_field.rows)
                if len(self.food_xy) >= self.food_max:
                    return
                if (x, y) not in self.snake_xy and (x, y) not in self.food_xy:
                    self.food_xy.append((x, y))
                    return

    def draw_food(self):
        """Draw food in game field."""
        self.food_sprites.clear()
        for index, xy in enumerate(self.food_xy):
            x = xy[0]*game_field.square_size + game_field.border
            y = xy[1]*game_field.square_size + game_field.border
            self.food_sprites.append(pyglet.sprite.Sprite(apple_image, x, y, batch=batch))
