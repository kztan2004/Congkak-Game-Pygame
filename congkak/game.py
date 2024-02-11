import pygame
from .constant import * 
from .board import Board

class Game:
    def __init__(self):
        self.win = WIN
        self.x = 0
        self.y = 0
        self.board = Board(self.win, LIGHT_CHOCO, DARK_CHOCO)

    def update(self):
        self.board.update()
    
    def get_pos(self, pos):
        return self.board.get_pos(pos)
    
    def select(self, pos):
        if pos == None:
            self.board.resetSelected()
        else:
            self.x, self.y = pos
            if self.x == 0 and self.board.turn == "UP":
                self.board.mark(self.x, self.y)
            if self.x == 1 and self.board.turn == "DOWN":
                self.board.mark(self.x, self.y)

    def choose(self):
        if self.board.choosed:
            if self.board.board[self.x][self.y].value != 0:
                self.board.resetSelected()
                self.move_cal(self.x, self.y)
    
    def move_cal(self, x_start, y_start):
        steps = self.board.board[x_start][y_start].value
        self.board.board[x_start][y_start].value = 0
        x = x_start
        y = y_start
        not_score = True
        while steps > 0:
            if x == 0:
                if y < 6:
                    y += 1
                    self.board.board[x][y].value += 1
                else:
                    if self.board.turn == "UP" and x == 0 and not_score:
                        self.board.right_score += 1
                        not_score = False
                    else:
                        x = 1
                        self.board.board[x][y].value += 1
                        not_score = True
            elif x == 1:
                if y > 0:
                    y -= 1
                    self.board.board[x][y].value += 1
                else:
                    if self.board.turn == "DOWN" and x == 1 and not_score:
                        self.board.left_score += 1
                        not_score = False
                    else:
                        x = 0
                        self.board.board[x][y].value += 1
                        not_score = True
            steps -= 1 
            pygame.time.delay(10)
            self.update()

        if not_score:
            if self.board.board[x][y].value > 1 :
                self.move_cal(x, y)
            else:
                self.board.change_turn()