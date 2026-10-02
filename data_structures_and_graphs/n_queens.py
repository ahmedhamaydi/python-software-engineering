def dfs_n_queens(n):
    solutions = []
    current = []

    def search(row):
        if row == n:
            solutions.append(current.copy())
            return

        for column in range(n):
            if column in current:
                continue

            # Check diagonals
            valid = True
            for previous_row, previous_column in enumerate(current):
                if abs(previous_row - row) == abs(previous_column - column):
                    valid = False
                    break

            if valid:
                current.append(column)
                search(row + 1)
                current.pop()

    search(0)
    return solutions