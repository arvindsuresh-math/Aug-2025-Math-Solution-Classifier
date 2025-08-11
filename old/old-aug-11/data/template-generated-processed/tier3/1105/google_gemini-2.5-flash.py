from fractions import Fraction

def solve():
    """Index: 1105.
    Returns: the amount of money Gina kept.
    """
    # L1
    initial_money = 400 # Gina had $400
    mom_fraction = Fraction(1, 4) # gave 1/4 of her money to her mom
    money_to_mom = mom_fraction * initial_money

    # L2
    clothes_fraction = Fraction(1, 8) # used 1/8 of her money to buy clothes
    money_for_clothes = clothes_fraction * initial_money

    # L3
    charity_fraction = Fraction(1, 5) # gave 1/5 of her money to a charity
    money_to_charity = charity_fraction * initial_money

    # L4
    total_spent = money_to_mom + money_for_clothes + money_to_charity

    # L5
    money_kept = initial_money - total_spent

    # FA
    answer = money_kept
    return answer