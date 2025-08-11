from fractions import Fraction

def solve():
    """Index: 971.
    Returns: the amount Annabelle saved.
    """
    # L1
    weekly_allowance = 30 # Annabelle collected a weekly allowance of $30
    junk_food_fraction = Fraction(1, 3) # spent a third of it
    junk_food_cost = weekly_allowance * junk_food_fraction

    # L2
    money_after_junk_food = weekly_allowance - junk_food_cost

    # L3
    sweets_cost = 8 # spent another $8 on sweets
    saved_amount = money_after_junk_food - sweets_cost

    # FA
    answer = saved_amount
    return answer