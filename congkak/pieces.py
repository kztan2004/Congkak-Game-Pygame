import pygame
from .constant import *

class Pieces:
    def __init__(self, row, col, value):
        self.color = DARK_CHOCO
        self.select_color = WHITE
        self.selected = False
        self.row = row
        self.col = col
        self.value = value
        self.rect = self.cal_pos()
    
    def cal_pos(self):
        x = WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (self.col * BOARD_WIDTH//7)
        if self.row == 0:
            y = HEIGHT//2 - BOARD_HEIGHT//4 + SMALL_GAP
        else:
            y = HEIGHT//2 + BOARD_HEIGHT//4 - SMALL_GAP
        
        return [x - SMALL_RADIUS, y - SMALL_RADIUS, x + SMALL_RADIUS, y + SMALL_RADIUS]
            