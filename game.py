
import pygame as pg

from objects import Snake, Food
import settings


class Game:
    def __init__(self):
        self.size = settings.GAME_WINDOW_SIZE
        self.bg_colour = settings.GAME_FILL_COLOUR
        self.tile_size = settings.TILE_SIZE
        self.surface = pg.Surface((self.size, self.size))
        self.score = 0
        self.level = 0
        self.new_game()
        self.pos_list = self.make_pos_list()

    def draw_grid(self):
        '''Blit our playing surface with a grid'''
        [pg.draw.line(self.surface,
                      [50]*3,
                      (x,0),
                      (x,self.size)) 
                      for x in range(0, self.size, self.tile_size)]
        [pg.draw.line(self.surface,
                      [50]*3,
                      (0,y),
                      (self.size,y)) 
                      for y in range(0, self.size, self.tile_size)]
        
    def make_pos_list(self):
        '''List of unoccupied squares by snake'''
        pos_list = []
        for x in range(0, self.size, self.tile_size):
            for y in range(0, self.size, self.tile_size):
                pos_list.append((x+self.tile_size//2, y+self.tile_size//2))

        segment_centres = [s.center for s in self.snake.segments]
        pos_list = [pos for pos in pos_list if pos not in segment_centres]
        return pos_list

    def new_game(self):
        '''Instantiate new Snake and Food objects'''
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0
        self.level = 0

    def draw(self):
        '''Draw all entities onto playing surface'''
        self.surface.fill(self.bg_colour)
        self.snake.draw()
        self.food.draw()
        self.draw_grid()

    def update(self):
        '''Update game'''
        self.snake.update()
        self.make_pos_list()
        self.draw()
