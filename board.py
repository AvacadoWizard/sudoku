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
    def __init__(self, board, answer=None):
        self.board = self.format_board(board)
        self.answer=None

    def format_board(self, board):
        final = [[] for i in range(9)]
        print(final)
        for line, char in enumerate(board):
            ind = (line)//9
            final[ind].append("   " if char == "0" else " " + char + " ")
        return final


    
    def print_board(self):
        line_break = "│─────────│─────────│─────────│"
        count = 0
        temp = ""
        for i in range(9):
            if (i%3 == 0):
                print(line_break)
            temp = ""
            for j in range(9):
                if (j%3 == 0):
                    temp = temp + "│"
                temp = temp + self.board[i][j]
            print(temp + "│")
        print(line_break)

            
b = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"



board = Board(b)
board.print_board()
print(board.board)

# solved_board = Board("864371259325849761971265843436192587198657432257483916689734125713528694542916378")
# solved_board.print_board()