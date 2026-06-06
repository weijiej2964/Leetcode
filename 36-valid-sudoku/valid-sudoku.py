class Solution:
    def isValidPlacement(self, board: List[List[str]], row, col) -> bool:
        for i in range(9):
            if (board[row][i] == board[row][col] and i != col) or (board[i][col] == board[row][col] and i != row):
                print(board[row][col] + " line")
                return False
        
        box_x = col // 3
        box_x *= 3
        box_y = row // 3
        box_y *= 3

        for i in range(box_y, box_y + 3):
            for k in range(box_x, box_x + 3):
                if board[i][k] == board[row][col] and (i != row and k != col):
                    print(box_y, "   ", box_x, "\n")
                    print(board[row][col] + "box")
                    return False

        
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] != "." and self.isValidPlacement(board, row, col) == False:
                    return False
                    
                    
        return True


                    