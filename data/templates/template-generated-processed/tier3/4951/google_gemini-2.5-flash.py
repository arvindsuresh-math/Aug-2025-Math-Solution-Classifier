from fractions import Fraction

def solve():
    """Index: 4951.
    Returns: the amount of money Joe has left.
    """
    # L1
    chocolate_fraction = Fraction(1, 9) # 1/9 of his pocket money
    total_pocket_money = 450 # pocket money of $450
    spent_on_chocolate = chocolate_fraction * total_pocket_money

    # L2
    fruit_fraction = Fraction(2, 5) # 2/5 on fruits
    spent_on_fruits = fruit_fraction * total_pocket_money

    # L3
    money_left = total_pocket_money - spent_on_chocolate - spent_on_fruits

    # FA
    answer = money_left
    return answer