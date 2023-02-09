# SNAKE GAME

import pyglet
from pyglet import gl
from pyglet.window import key


from images_load import batch
from game_state import GameState
from field import game_field


TIME_TO_MOVE = [0.7]


def on_key_press(symbol, modifiers):
    """User press key for setting the snake direction."""
    if symbol == key.LEFT:
        game_state.direction = (-1, 0)
    if symbol == key.RIGHT:
        game_state.direction = (1, 0)
    if symbol == key.UP:
        game_state.direction = (0, 1)
    if symbol == key.DOWN:
        game_state.direction = (0, -1)
    if symbol == key.ENTER:
        game_state.keys.append(('enter', 0))


def on_key_release(symbol, modifiers):
    """On key release."""
    if symbol == key.ENTER:
        game_state.keys.clear()


def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)
    gl.glLineWidth(4)

    x1 = game_field.origin_xy0_game_field[0]
    y1 = game_field.origin_xy0_game_field[1]
    x2 = game_field.origin_xy1_game_field[0]
    y2 = game_field.origin_xy1_game_field[1]
    draw_polygon((x1, y1), (x1, y2), (x2, y2), (x2, y1))

    x1 = game_field.origin_xy0_menu[0]
    y1 = game_field.origin_xy0_menu[1]
    x2 = game_field.origin_xy1_menu[0]
    y2 = game_field.origin_xy1_menu[1]
    draw_polygon((x1, y1), (x1, y2), (x2, y2), (x2, y1))

    batch.draw()

    menu_text()

    if game_state.state == 'dead':
        dead_text()

    if game_state.state == 'game_over':
        game_over_text()


def dead_text():
    draw_text('For continue set valid direction',
              x=game_field.size_window()[0]//2,
              y=game_field.size_window()[1]//2-100,
              size=30,
              anchor_x='center')

def menu_text():
    draw_text('in Python',
              x=game_field.origin_xy0_menu[0]+25,
              y=game_field.origin_xy1_menu[1]-130,
              size=16,
              anchor_x='left')
    draw_text('Move with ← ↓ ↑ →',
              x=game_field.origin_xy0_menu[0]+300,
              y=game_field.origin_xy1_menu[1]-50,
              size=16,
              anchor_x='left')
    draw_text('Eat Apples',
              x=game_field.origin_xy0_menu[0]+300,
              y=game_field.origin_xy1_menu[1]-80,
              size=16,
              anchor_x='left')
    draw_text('Don\'t eat walls or yourself.',
              x=game_field.origin_xy0_menu[0]+300,
              y=game_field.origin_xy1_menu[1]-110,
              size=16,
              anchor_x='left')
    draw_text(str(game_state.lives),
              x=game_field.origin_xy1_menu[0]-70,
              y=game_field.origin_xy1_menu[1]-65,
              size=30,
              anchor_x='left')
    draw_text(str(len(game_state.snake_xy)),
              x=game_field.origin_xy1_menu[0]-70,
              y=game_field.origin_xy1_menu[1]-115,
              size=30,
              anchor_x='left')


def game_over_text():
    draw_text('GAME  OVER',
              x=game_field.size_window()[0]//2,
              y=game_field.size_window()[1]//2-100,
              size=30,
              anchor_x='center')
    draw_text('Press ENTER',
              x=game_field.size_window()[0]//2,
              y=game_field.size_window()[1]//2-140,
              size=20,
              anchor_x='center')


def move(t):
    TIME_TO_MOVE[0] -= t
    if TIME_TO_MOVE[0] < 0:
        game_state.move(t)
        if game_state.state == 'game_over' and ('enter', 0) in game_state.keys:
            game_state.restart_conditions()
        time = max(0.7 - 0.05 * int(len(game_state.snake_xy))/3, 0.2)
        TIME_TO_MOVE[0] = time


def reset():
    game_state = GameState()
    game_state.draw_snake_parts()
    return game_state


def draw_polygon(xy1, xy2, xy3, xy4):
    """Draw polygon."""
    gl.glBegin(gl.GL_LINE_LOOP);
    gl.glVertex2f(int(xy1[0]), int(xy1[1]));
    gl.glVertex2f(int(xy2[0]), int(xy2[1]));
    gl.glVertex2f(int(xy3[0]), int(xy3[1]));
    gl.glVertex2f(int(xy4[0]), int(xy4[1]));
    gl.glEnd();


def draw_text(text, x, y, size, anchor_x):
    """Draw text in game field."""
    text = pyglet.text.Label(
        text,
        font_name='Arial',
        font_size=size,
        x=x, y=y, anchor_x=anchor_x)
    text.draw()


window = pyglet.window.Window(game_field.size_window()[0], game_field.size_window()[1])


game_state = reset()


window.push_handlers(
    on_draw=on_draw,
    on_key_press=on_key_press,
)


pyglet.clock.schedule_interval(move, 1/30)
pyglet.clock.schedule_interval(game_state.add_food, 5)


pyglet.app.run()
