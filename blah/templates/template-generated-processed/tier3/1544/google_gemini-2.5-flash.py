from fractions import Fraction

def solve():
    """Index: 1544.
    Returns: the amount of money Ben has left after expenses.
    """
    # L1
    bonus_amount = 1496 # Ben will receive a bonus of $1496
    kitchen_fraction = Fraction(1, 22) # 1/22 for the kitchen
    kitchen_spending = bonus_amount * kitchen_fraction

    # L2
    holiday_fraction = Fraction(1, 4) # 1/4 for holidays
    holiday_spending = bonus_amount * holiday_fraction

    # L3
    gifts_fraction = Fraction(1, 8) # 1/8 for Christmas gifts
    gifts_spending = bonus_amount * gifts_fraction

    # L4
    total_spent = kitchen_spending + holiday_spending + gifts_spending

    # L5
    money_left = bonus_amount - total_spent

    # FA
    answer = money_left
    return answer