def solve():
    """Index: 6963.
    Returns: the amount of money the saleswoman returns to Leila.
    """
    # L1
    apples_cost = 5 # apples for 5€
    sugar_cost = 3 # sugar for 3€
    carrots_cost = 17 # carrots for 17€
    total_spent = apples_cost + sugar_cost + carrots_cost

    # L2
    paid_amount = 50 # paid with a 50€ bill
    change_returned = paid_amount - total_spent

    # FA
    answer = change_returned
    return answer