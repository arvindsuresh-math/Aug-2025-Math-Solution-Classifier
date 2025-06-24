def solve():
    """
    Solves the problem to find how many digits Sam memorized.

    Mina memorized 24 digits of pi.
    Mina memorized six times as many digits as Carlos.
    Sam memorized six more digits than Carlos.
    """

    mina_digits = 24

    # L1: Calculate how many digits Carlos memorized.
    # Mina memorized 6 times what Carlos memorized, so Carlos's digits = Mina's digits / 6.
    carlos_digits = mina_digits / 6

    # L2: Calculate how many digits Sam memorized.
    # Sam memorized 6 more digits than Carlos.
    sam_digits = carlos_digits + 6

    return int(sam_digits)

# The final answer is the result of the solve() function.
# print(solve())