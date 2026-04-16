class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # This part could be made dynamic with collections.defaultdict instead of manual keys
        # But it is fine as sudoku is always 3x3.
        rows = [set() for _ in range(len(board))]   # Key: row, Val: nums
        cols = [set() for _ in range(len(board))]   # Key: col, Val: nums
        boxes = {(0,0):set(), (0,1):set(), (0,2):set(), (1,0):set(), (1,1):set(), (1,2):set(), (2,0):set(), (2,1):set(), (2,2):set()}  # Key: (row//3, col//3) = [0/1/2][0/1/2], Val: nums

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row//3, col//3)]:
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    boxes[(row//3, col//3)].add(board[row][col])
        
        return True     