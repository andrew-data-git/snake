import pygame as pg
import sys

from game import Game
import settings

class App():
    def __init__(self, display):
        self.window_size = (settings.APP_WINDOW_WIDTH, settings.APP_WINDOW_HEIGHT) 
        self.window_colour = settings.APP_WINDOW_COLOUR
        self.display = display
        self.base_font = pg.font.Font(None, 36)
        self.info_surface = pg.Surface((settings.INFO_WIDTH, settings.INFO_HEIGHT))
        self.info_rect = self.info_surface.get_rect()
        self.clock = pg.time.Clock()
        self.game = Game()

    def draw(self):
        '''Draw application'''
        self.display.fill(self.window_colour)
        self.display.blit(self.info_surface, (settings.GAME_WINDOW_SIZE+2*settings.PADDING, 
                                              settings.PADDING))
        self.display.blit(self.game.surface, (settings.PADDING, settings.PADDING))
    
    def populate_info(self):
        '''Populate info bar with information'''
        self.info_surface.fill(settings.INFO_COLOUR)  # Example: Fill with a solid color

        font = pg.font.Font(None, 36)
        title_text = "Snake game"
        score_text = str(self.game.score)

        title_surface = font.render(title_text, True, settings.TEXT_COLOUR)
        title_rect = title_surface.get_rect()
        title_rect.midtop = (self.info_rect.width // 2, 10)

        score_surface = font.render(score_text, True, settings.TEXT_COLOUR)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (self.info_rect.width // 2, title_rect.bottom + 10)  # Center horizontally, below the title

        # Blit the text onto the info_surface
        self.info_surface.blit(title_surface, title_rect)
        self.info_surface.blit(score_surface, score_rect)

    def update(self):
        '''Update application'''
        self.clock.tick(settings.FPS)
        self.game.update()
        self.populate_info()
        pg.display.flip()

    def check_event(self): # TODO something is wrong here!!!! keystrokes are not all being logged
        '''Parse events'''
        for event in pg.event.get():
            print('app', event)
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        '''Run application'''
        while True:
            self.game.run()
            self.check_event()
            self.update()
            self.draw()