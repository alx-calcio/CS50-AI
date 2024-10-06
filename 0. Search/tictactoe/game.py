import math
from settings import EMPTY, X, O

class Game:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(3)] for _ in range(3)]

    
    def __str__(self):
        string = ""
        for line in self.grid:
            for character in line:
                string += f"{character if character else "_"} "
            string += "\n"
        return string

    def play(self, x, y):
        self.grid = self.result(self.grid, (x,y))
        
        
    def result(self, board, action):
        if action not in self.actions(board):
            raise Exception("Invalid action", action, board, self.actions(board))
        new_board = [row[:] for row in board]
        new_board[action[1]][action[0]] = self.player(board)
        return new_board
    
    def player(self, board):
        cnt_X = 0
        cnt_O = 0
        for i in range(3):
            for j in range(3): 
                if board[i][j] == X:
                    cnt_X += 1
                elif board[i][j] == O:
                    cnt_O += 1

        if cnt_X == cnt_O:
            return X
        elif cnt_X > cnt_O:
            return O
        else:
            return X

    def actions(self, board):
        actions = []
        for x in range(3):
            for y in range(3):
                if board[y][x] == EMPTY:
                    actions.append((x, y))
        return actions

    def winner(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                    return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != EMPTY:
                    return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != EMPTY:
                return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != EMPTY:
                return board[0][2]
        return None
    
    def terminal(self, board):
        if self.winner(board):
            return True
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        return False
            return True
    
    def utility(self, board):
        if self.winner(board) == X:
            return 1
        elif self.winner(board) == O:
            return -1
        else:
            return 0
        
    def max_value(self, board, alpha, beta):
        if self.terminal(board):
            return self.utility(board)
        v = -math.inf
        for action in self.actions(board):
            v = max(v, self.min_value(self.result(board, action), alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v

    def min_value(self, board, alpha, beta):
        if self.terminal(board):
            return self.utility(board)
        v = math.inf
        for action in self.actions(board):
            v = min(v, self.max_value(self.result(board, action), alpha, beta))
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v

    def minimax(self, board):
        if self.terminal(board):
            return None
        if self.player(board) == X:
            v = -math.inf
            opt_action = None
            for action in self.actions(board):
                new_value = self.min_value(self.result(board, action), -math.inf, math.inf)
                if new_value > v:
                    v = new_value
                    opt_action = action
            return opt_action
        
        elif self.player(board) == O:
            v = math.inf
            opt_action = None
            for action in self.actions(board):
                new_value = self.max_value(self.result(board, action), -math.inf, math.inf)
                if new_value < v:
                    v = new_value
                    opt_action = action
            return opt_action
