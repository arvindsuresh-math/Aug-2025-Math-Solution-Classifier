from fractions import Fraction

def solve():
    """Index: 2158.
    Returns: the amount of money the housewife has left.
    """
    # L1
    total_fraction = Fraction(3, 3) # WK
    spent_fraction = Fraction(2, 3) # spent 2/3 of her $150
    remaining_fraction = total_fraction - spent_fraction

    # L2
    initial_money = 150 # her $150
    money_left = initial_money * remaining_fraction

    # FA
    answer = money_left
    return answer