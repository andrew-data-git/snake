
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
        self.new_game()

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

    def new_game(self):
        '''Instantiate new Snake and Food objects'''
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0

    def draw(self):
        '''Draw all entities onto playing surface'''
        # self.display.blit(self.surface, (settings.PADDING, settings.PADDING))
        self.surface.fill(self.bg_colour)
        self.snake.draw()
        self.food.draw()
        self.draw_grid()

    def update(self):
        '''Update game'''
        self.snake.update()

    def snake_controls(self):
        '''Parse events'''
        for event in pg.event.get():
            print('game', event)
            self.snake.control(event)

    def run(self):
        '''Run game'''
        self.snake_controls()
        self.update()
        self.draw()