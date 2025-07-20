from fractions import Fraction

def solve():
    """Index: 4150.
    Returns: the amount of money Mrs. Thomson saved.
    """
    # L1
    total_incentive = 240 # Mrs. Thomson received an incentive worth $240
    food_fraction = Fraction(1, 3) # spent 1/3 of the money on food
    spent_on_food = total_incentive * food_fraction

    # L2
    clothes_fraction = Fraction(1, 5) # and 1/5 of it on clothes
    spent_on_clothes = total_incentive * clothes_fraction

    # L3
    total_spent_on_items = spent_on_food + spent_on_clothes

    # L4
    remaining_money_after_items = total_incentive - total_spent_on_items

    # L5
    savings_fraction = Fraction(3, 4) # put in her savings account 3/4 of the remaining money
    money_saved = remaining_money_after_items * savings_fraction

    # FA
    answer = money_saved
    return answer