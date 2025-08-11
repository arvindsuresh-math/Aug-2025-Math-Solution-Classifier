def solve():
    """Index: 216.
    Returns: the amount of money Missy put in the bank the first year, in dollars.
    """
    # L5
    total_amount = 450 # it contained $450 in change
    # x is the amount in the first year (unknown)
    # L6
    sum_coeff = 15 # 1 + 2 + 4 + 8 = 15
    # L7
    x = total_amount // sum_coeff
    # FA
    answer = x
    return answer