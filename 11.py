def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue

            box_index = (i // 3) * 3 + (j // 3)

            if (val in rows[i]) or (val in cols[j]) or (val in boxes[box_index]):
                return False

            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)

    return True



board1 = [
    ["8", "3", "7", "1", "9", "5", ".", ".", "."],
    ["6", "1", "9", "5", "8", "3", ".", ".", "."],
    ["9", "8", "6", "3", "1", "7", ".", ".", "."],
    ["8", "6", "3", "1", "9", "5", ".", ".", "."],
    ["4", "1", "8", "3", "7", "9", ".", ".", "."],
    ["7", "1", "9", "5", "8", "3", ".", ".", "."],
    ["6", "3", "1", "9", "5", ".", ".", ".", "."],
    ["8", "3", "7", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

print(is_valid_sudoku(board1))