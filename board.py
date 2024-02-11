class Board:
    def __init__(self, n):
        self.n = n
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.MAX_MOVES = n * n
        self.move_count = 0
        self.show_board()

    def is_move_valid(self, row, col):
        return self.board[row][col] is None

    def make_move(self, row, col, piece):
        self.board[row][col] = piece
        self.move_count += 1
        self.show_board()

    def no_valid_moves_left(self):
        return self.move_count == self.MAX_MOVES

    def has_player_won(self, row, col, piece):
        return (self.row_check(row, piece) or
                self.col_check(col, piece) or
                self.pos_diagonal_check(row, col, piece) or
                self.neg_diagonal_check(row, col, piece))

    def row_check(self, row, piece):
        for j in range(self.n):
            if self.board[row][j] != piece:
                return False
        return True

    def col_check(self, col, piece):
        for i in range(self.n):
            if self.board[i][col] != piece:
                return False
        return True

    def pos_diagonal_check(self, row, col, piece):
        if row != col:
            return False
        for i in range(self.n):
            if self.board[i][i] != piece:
                return False
        return True

    def neg_diagonal_check(self, row, col, piece):
        if row + col != self.n - 1:
            return False
        for i in range(self.n):
            if self.board[i][self.n-1-i] != piece:
                return False
        return True

    def show_board(self):
        for row in self.board:
            print(' '.join([cell if cell is not None else '-' for cell in row]))
