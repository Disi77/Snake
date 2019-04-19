# ClASS for Game field

class Game_field():
    '''
    Game field class.
    '''
    def __init__(self):
        '''
        Input values for Game field.
        '''
        self.square_size = 64
        self.rows = 8
        self.collums = 12
        self.border = self.square_size//2
        self.menu_height = 150
        self.menu_width = self.collums*self.square_size
        self.origin_xy0_game_field = (0+self.border, 0+self.border)
        self.origin_xy1_game_field = (0+self.border + self.collums*self.square_size, 0+self.border + self.rows*self.square_size)
        self.origin_xy0_menu = (0+self.border, 0+2*self.border+self.rows*self.square_size)
        self.origin_xy1_menu = (0+self.border + self.collums*self.square_size, 0+2*self.border+self.rows*self.square_size + self.menu_height)

    def size_window(self):
        '''
        Window, Game field and Menu size in pixels.
       __ __ __ __ __ ___ __ __ __ __
      |  __ __ __ __ __ __ __ __ __   |
      | |                           | |
      | |         menu              | |
      | |__ __ __ __ __ __ __ __ __ | |
      |   __ __ __ __ __ __ __ __ __  |
      | |                           | |
      | |                           | |
      | |          Game             | |
      | |         field             | |
      | |                           | |
      | |__ __ __ __ __ __ __ __ __ | |
      |__ __ __ __ __ ___ __ __ __ __ |

        '''
        window_height = self.square_size * self.collums + 2*self.border
        window_width = self.square_size * self.rows + 3*self.border + self.menu_height
        return (window_height, window_width)


game_field = Game_field()
