def solve():
    """Index: 4308.
    Returns: the total number of rolls John bought.
    """
    # L1
    total_spent = 15 # He spent 15 dollars
    cost_per_dozen = 5 # sell them for 5 dollars for a dozen
    dozens_bought = total_spent / cost_per_dozen

    # L2
    rolls_per_dozen = 12 # WK
    total_rolls = dozens_bought * rolls_per_dozen

    # FA
    answer = total_rolls
    return answer