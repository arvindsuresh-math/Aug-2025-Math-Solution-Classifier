from fractions import Fraction

def solve():
    """Index: 6461.
    Returns: the amount of money John had left.
    """
    # L1
    mother_fraction = Fraction(3, 8) # 3/8 of his money
    initial_money = 200 # John had $200
    money_to_mother = mother_fraction * initial_money

    # L2
    father_fraction = Fraction(3, 10) # 3/10 to his father
    money_to_father = father_fraction * initial_money

    # L3
    total_given_away = money_to_mother + money_to_father

    # L4
    money_left = initial_money - total_given_away

    # FA
    answer = money_left
    return answer