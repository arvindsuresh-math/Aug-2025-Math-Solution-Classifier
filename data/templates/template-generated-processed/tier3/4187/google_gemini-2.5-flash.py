from fractions import Fraction

def solve():
    """Index: 4187.
    Returns: the amount of money Jeremy has remaining after the purchase.
    """
    # L1
    money_multiplier = 2 # two times more money
    computer_price = 3000 # a computer for $3000
    initial_money = money_multiplier * computer_price

    # L2
    accessories_fraction = Fraction(1, 10) # 10% of the price
    accessories_cost = computer_price * accessories_fraction

    # L3
    money_remaining = initial_money - computer_price - accessories_cost

    # FA
    answer = money_remaining
    return answer