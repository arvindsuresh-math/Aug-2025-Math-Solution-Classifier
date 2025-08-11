def solve():
    """Index: 4074.
    Returns: the amount of change the saleswoman will give back.
    """
    # L1
    pants_cost = 140 # $140 worth of pants
    shirt_cost = 43 # a $43 shirt
    tie_cost = 15 # a $15 tie
    total_expenses = pants_cost + shirt_cost + tie_cost

    # L2
    paid_amount = 200 # a $200 bill
    change_back = paid_amount - total_expenses

    # FA
    answer = change_back
    return answer