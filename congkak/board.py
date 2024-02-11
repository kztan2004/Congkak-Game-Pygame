import pygame
from .pieces import Pieces
from .constant import *

class Board:
    def __init__(self, win, color, side_color):
        self.color = color
        self.side_color = side_color
        self.win = win
        self._init()

    def _init(self):
        self.board = []
        self._create_board()
        self.finish = False
        self.turn = "UP"
        self.choosed = False
        self.left_score = 0
        self.right_score = 0
    
    def reset(self):
        self._init()
        
    def change_turn(self):
        if self.turn == "DOWN":
            self.turn = "UP"
        else:
            self.turn = "DOWN"
    
    def _check_win(self):
        upttl = 0
        dwnttl = 0
        for piece1 in self.board[0]:
            upttl += piece1.value
        for piece2 in self.board[1]:
            dwnttl += piece2.value
        if upttl == 0 and dwnttl == 0:
            self.finish = True
        elif upttl == 0:
            self.turn = "DOWN"
        elif dwnttl == 0:
            self.turn = "UP"

    def draw(self):
        self._draw_board()
        self._draw_pieces()
        self._draw_score()
        self._draw_turn(self.turn)
        self._winner()

    def _draw_board(self):
        pygame.draw.circle(self.win, self.color,(WIDTH//2 - BOARD_WIDTH//2, HEIGHT//2), RADIUS)
        pygame.draw.circle(self.win, self.color,(WIDTH//2 + BOARD_WIDTH//2, HEIGHT//2), RADIUS)
        pygame.draw.circle(self.win, self.side_color,(WIDTH//2 - BOARD_WIDTH//2, HEIGHT//2), RADIUS - PADDING)
        pygame.draw.circle(self.win, self.side_color,(WIDTH//2 + BOARD_WIDTH//2, HEIGHT//2), RADIUS - PADDING)
        pygame.draw.rect(self.win, self.color, (WIDTH//2 - BOARD_WIDTH//2, HEIGHT//2 - BOARD_HEIGHT//2, BOARD_WIDTH, BOARD_HEIGHT))

    def _draw_pieces(self):
        font = pygame.font.SysFont("comicsans", 35)
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col].selected:
                    if row == 0:
                        pygame.draw.circle(self.win, RED, (WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7), HEIGHT//2 - BOARD_HEIGHT//4 + SMALL_GAP), SMALL_RADIUS+PADDING//5)
                    else:
                        pygame.draw.circle(self.win, BLUE, (WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7), HEIGHT//2 + BOARD_HEIGHT//4 - SMALL_GAP), SMALL_RADIUS+PADDING//5)
                if row == 0:
                    pygame.draw.circle(self.win, self.side_color, (WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7), HEIGHT//2 - BOARD_HEIGHT//4 + SMALL_GAP), SMALL_RADIUS)
                    text = font.render(str(self.board[row][col].value), 1, (255,255,255))
                    self.win.blit(text,(WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7) - text.get_width()//2, HEIGHT//2 - BOARD_HEIGHT//4 + SMALL_GAP - text.get_height()//2))
                else:
                    pygame.draw.circle(self.win, self.side_color, (WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7), HEIGHT//2 + BOARD_HEIGHT//4 - SMALL_GAP), SMALL_RADIUS)
                    text = font.render(str(self.board[row][col].value), 1, (255,255,255))
                    self.win.blit(text,(WIDTH//2 - BOARD_WIDTH//2 + SMALL_RADIUS + SMALL_PADDING + (col * BOARD_WIDTH//7) - text.get_width()//2, HEIGHT//2 + BOARD_HEIGHT//4 - SMALL_GAP - text.get_height()//2))

    def _draw_score(self):
        font = pygame.font.SysFont("comicsans", 35)
        left_score_text = font.render(str(self.left_score), 1, WHITE)
        self.win.blit(left_score_text,(WIDTH//2 - BOARD_WIDTH//2 - RADIUS//2 + PADDING - left_score_text.get_width()//2, HEIGHT//2 - left_score_text.get_height()//2))
        right_score_text = font.render(str(self.right_score), 1, WHITE)
        self.win.blit(right_score_text,(WIDTH//2 + BOARD_WIDTH//2 + RADIUS//2 - PADDING - left_score_text.get_width()//2, HEIGHT//2 - left_score_text.get_height()//2))
    
    def _draw_turn(self, turn):
        font = pygame.font.SysFont("comicsans", 35)
        if turn == "DOWN":
            text = font.render("DOWN TURN", 1, BLACK)
            pygame.draw.rect(self.win, BLUE, (WIDTH//2 - TURN_WIDTH//2, HEIGHT - TURN_HEIGHT, TURN_WIDTH, TURN_HEIGHT))
        else:
            text = font.render("UP TURN", 1, BLACK)
            pygame.draw.rect(self.win, RED, (WIDTH//2 - TURN_WIDTH//2, HEIGHT - TURN_HEIGHT, TURN_WIDTH, TURN_HEIGHT))
        self.win.blit(text,(WIDTH//2 - text.get_width()//2, HEIGHT - TURN_HEIGHT//2 - text.get_height()//2))
    
    def draw_result(self, winner):
        font = pygame.font.SysFont("comicsans", 80)
        if winner == "UP":
            text = font.render("UP WIN", 1, BLACK) 
            color = RED
        elif winner == "DOWN":
            text = font.render("DOWN WIN", 1, BLACK) 
            color = BLUE
        else:
            text = font.render("DRAW", 1, BLACK) 
            color = GREY
        pygame.draw.rect(self.win, color, (WIDTH//2 - BOARD_WIDTH//2 + PADDING, HEIGHT//2 - BOARD_HEIGHT//2 + PADDING, BOARD_WIDTH - 2 * PADDING, BOARD_HEIGHT - 2 * PADDING))
        self.win.blit(text,(WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

    def _winner(self):
        if self.finish:
            if self.left_score == self.right_score:
                self.draw_result("DOWN")
            elif self.left_score > self.right_score:
                self.draw_result( "DOWN")
            else:
                self.draw_result("UP")

    def _create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Pieces(row, col, VALUE))

    def get_pos(self, pos):
        x, y = pos
        for row in range(ROWS):
            for col in range(COLS):
                rect_pos = self.board[row][col].rect
                if rect_pos[0] <= x <= rect_pos[2] and rect_pos[1] <= y <= rect_pos[3]:
                    return row, col
        return None

    def mark(self, x, y):
        self.resetSelected()
        self.board[x][y].selected = True
        self.choosed = True

    def resetSelected(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row][col].selected = False
        self.choosed = False
    
    def update(self):
        self.win.fill(WHITE)
        self._check_win()
        self.draw()
        pygame.display.update()
        if self.finish:
            pygame.time.delay(5000)
            self.reset()