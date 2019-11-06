from helpers.bit_operations import *

# Function to check whether it is safe to place the queen at this spot by checking the two diagonals and the column.
def is_safe(n, row, col, col_checker, diag1_checker, diag2_checker):
    return not is_kth_bit_set(col_checker, col) and \
           not is_kth_bit_set(diag1_checker, row - col + n - 1) and \
           not is_kth_bit_set(diag2_checker, row + col)

# Placing the queen by marking the column and the two diagonals as occupied
def place_queen(n, row, col, col_checker, diag1_checker, diag2_checker):
    col_checker = set_kth_bit(col_checker, col)
    diag1_checker = set_kth_bit(diag1_checker, row - col + n - 1)
    diag2_checker = set_kth_bit(diag2_checker, row + col)
    return col_checker, diag1_checker, diag2_checker

# Unplace the queen by freeing up the column and the two diagonals
def unplace_queen(n, row, col, col_checker, diag1_checker, diag2_checker):
    col_checker = unset_kth_bit(col_checker, col)
    diag1_checker = unset_kth_bit(diag1_checker, row - col + n - 1)
    diag2_checker = unset_kth_bit(diag2_checker, row + col)
    return col_checker, diag1_checker, diag2_checker


def solve(n, row, col_checker, diag1_checker, diag2_checker, ans):
    if row == n: # base case
        return ans + 1
    for col in range(0, n):
        if is_safe(n, row, col, col_checker, diag1_checker, diag2_checker):
            col_checker, diag1_checker, diag2_checker = \
                place_queen(n, row, col,
                            col_checker, diag1_checker, diag2_checker)
            ans = solve(n, row + 1, col_checker, diag1_checker, diag2_checker, ans) # recursive call
            col_checker, diag1_checker, diag2_checker = \
                unplace_queen(n, row, col,
                              col_checker, diag1_checker, diag2_checker)
    return ans


def runner(n):
    return solve(n, 0, 0, 0, 0, 0)
