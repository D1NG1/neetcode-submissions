class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for current in row:
                if current in seen and current != ".":
                    return False
                else:
                    seen.add(current)
        
        for i in range(9):
            seen = set()
            for j in range(9):
                current = board[j][i]
                if current in seen and current != ".":
                    return False
                else:
                    seen.add(current)
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) *3 +i
                    col = (square%3) *3 +j
                    current = board[row][col]
                    if current in seen and current != ".":
                        return False
                    else:
                        seen.add(current)   

        return True
        

        