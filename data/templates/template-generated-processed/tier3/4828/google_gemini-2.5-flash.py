from fractions import Fraction

def solve():
    """Index: 4828.
    Returns: the amount of money John has left.
    """
    # L1
    initial_money = 20 # John had $20
    snack_fraction = Fraction(1, 5) # 1/5 of his money on snacks
    money_spent_on_snacks = initial_money * snack_fraction

    # L2
    money_remaining_after_snacks = initial_money - money_spent_on_snacks

    # L3
    necessities_fraction = Fraction(3, 4) # 3/4 of the remaining money on necessities
    money_spent_on_necessities = money_remaining_after_snacks * necessities_fraction

    # L4
    money_left = money_remaining_after_snacks - money_spent_on_necessities

    # FA
    answer = money_left
    return answer