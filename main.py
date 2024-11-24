
import pygame as pg

from app import App
import settings

DISPLAY = pg.display.set_mode([settings.APP_WINDOW_WIDTH, settings.APP_WINDOW_HEIGHT])
pg.display.set_caption('Snake')
if __name__ == '__main__':
    pg.init()
    app = App(DISPLAY)
    app.run()