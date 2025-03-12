# https://www.kaggle.com/datasets/bryanpark/sudoku/data

""""
│───────────│───────────│───────────│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│───────────│───────────│───────────│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│───────────│───────────│───────────│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│---|---|---│---|---|---│---|---|---│
│───────────│───────────│───────────│


"""

class Board():
    def __init__(self, board):
        self.board = self.format_board(board)
        self.answer = self.format_board(board)

    def format_board(self, board):
        final = [[] for i in range(9)]
        for line, char in enumerate(board):
            ind = (line)//9
            final[ind].append(char)
        return final

    def print_board(self):
        self.print_method(self.board)
    
    def print_answer(self):
        self.print_method(self.answer)
    
    def print_method(self, board):
        line_break = "│─────────│─────────│─────────│"
        temp = ""
        for i in range(9):
            if (i%3 == 0):
                temp += line_break + "\n"
            for j in range(9):
                if (j%3 == 0):
                    temp = temp + "│"
                temp = temp + " " + board[i][j] + " " if board[i][j] != "0" else temp +  "   "
            temp += "│" + "\n"
        temp += line_break + "\n"

        print(temp)

    def is_safe(self, board, r, c, num):
        # check if taken up
        if board[r][c] != "0":
            print(board[r][c])
            print("ahhh")
            return False
        # check the row
        for i in board[r]:
            if i == num:
                return False
        # check the column
        for i in range(9):
            if board[i][c] == num:
                return False
        # check the square
        start_r = r - (r%3)
        start_c = c - (c%3)
        for i in range(3):
            for j in range(3):
                if board[i  + start_r][j + start_c] == num:
                    return False
        return True
    
    def solve(self, board,  r = 0, c = 0):
        # Base Case
        if r == 8 and c == 9:
            return True
        
        if c == 9:
            r += 1
            c = 0
        # Recursive Case

        if board[r][c] != "0":
            return self.solve(board, r, c+1)

        for i in range(9):
            if self.is_safe(board, r, c, str(i+1)):
                board[r][c] = str(i+1)
                self.answer[r][c] = str(i+1)
                if self.solve(board, r, c+1):
                    return True
                self.answer[r][c] = "0"
                board[r][c] = "0"
                

        return False
                
                



            
b = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"



board = Board(b)
print("Initial Board") 
board.print_board()
print("after solving")
print(board.solve(board.board))
board.print_answer()

# board.board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
# board.print_board()

# def isValidSudoku(board) -> bool:
#     for r in range(len(board)):
#         for c in range(9):
#             curr = board[r][c]
#             if curr == ".":
#                 break
#             for i in range(9):
#                 if curr == board[r][i] and i != c:
#                     print("False due to column")
#                     return False
#                 print(board[i][c], board[r][c])
#                 if curr == board[i][c] and i != r:
#                     print("False due to row")
#                     return False
#             start_row = r - r % 3
#             start_col = c - c % 3
#             for i in range(3):
#                 for j in range(3):
#                     if curr == board[start_row + i][start_col + j] and i != r and j != c:
#                         print(r, c)
#                         print(start_row + i, start_col + j)
#                         print(board[r][c])
#                         print(board[start_row + i][start_col + j])
#                         return False
#     return True

# print(isValidSudoku(board.board))
# print(board.board[3][3])
# print(board.board[6][3])