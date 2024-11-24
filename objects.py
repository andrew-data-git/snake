import pygame as pg
from random import randrange

import settings

vec2 = pg.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.tile_size
        self.rect = pg.rect.Rect([0, 0, game.tile_size-5, game.tile_size-5])
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100 # ms
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pg.K_w:1, pg.K_s:1, pg.K_a:1, pg.K_d:1}
        self.colour = settings.SNAKE_COLOUR

    def control(self, event):
        '''Send keystrokes to snake'''
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pg.K_w:1, pg.K_s:0, pg.K_a:1, pg.K_d:1}
            elif event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pg.K_w:0, pg.K_s:1, pg.K_a:1, pg.K_d:1}
            elif event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pg.K_w:1, pg.K_s:1, pg.K_a:1, pg.K_d:0}
            elif event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions = {pg.K_w:1, pg.K_s:1, pg.K_a:0, pg.K_d:1}

    def check_food(self):
        '''Check if the snake's head occupies same tile as food'''
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1
            self.game.score += 10

    def delta_time(self):
        '''Match movement to FPS'''
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def get_random_position(self):
        '''Helper function to redraw snake objects'''
        vals = self.size//2, self.game.size - self.size//2, self.size  
        return [randrange(*vals)]*2
    
    def move(self):
        '''Move snake based on direction attribute'''
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def check_borders(self):
        '''Snake must remain in playing surface'''
        if self.rect.left < 0 or self.rect.right > self.game.size:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.size:
            self.game.new_game()

    def check_selfeating(self):
        '''Compare set of segments; if length different then snake overlaps self'''
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def update(self):
        '''Snake update'''
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        '''Draw the snake segments'''
        [pg.draw.rect(self.game.surface, self.colour, segment) for segment in self.segments]


class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.tile_size
        self.rect = pg.rect.Rect([0, 0, game.tile_size-20, game.tile_size-20])
        self.rect.center = self.game.snake.get_random_position()
        self.colour = settings.FOOD_COLOUR

    def draw(self):
        '''Draw food'''
        pg.draw.rect(self.game.surface, self.colour, self.rect)