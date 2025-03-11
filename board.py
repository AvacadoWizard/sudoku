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
        if r == 9:
            return True
        
        # Recursive Case

        if c == 9:
            r += 1
            c = 0

        for i in range(9):
            if self.is_safe(board, r, c, str(i)):
                board[r][c] = str(i)
                if self.solve(board, r, c+1):
                    self.answer[r][c] = str(i)
                    return True
                board[r][c] = "0"

        return False
                
                



            
b = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"



board = Board(b)
print("Initial Board") 
board.print_board()
board.print_board()

# solved_board = Board("864371259325849761971265843436192587198657432257483916689734125713528694542916378")
# solved_board.print_board()