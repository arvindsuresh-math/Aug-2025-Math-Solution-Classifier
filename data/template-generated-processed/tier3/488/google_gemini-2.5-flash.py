from fractions import Fraction

def solve():
    """Index: 488.
    Returns: the amount of money Mrs. Smith still needs.
    """
    # L1
    initial_money = 500 # worth $500
    fraction_more = Fraction(2, 5) # two-fifths more money
    additional_money_needed = fraction_more * initial_money

    # L2
    total_cost_before_discount = additional_money_needed + initial_money

    # L3
    discount_percentage = Fraction(15, 100) # discount of 15%
    discount_amount = discount_percentage * total_cost_before_discount

    # L4
    cost_after_discount = total_cost_before_discount - discount_amount

    # L5
    money_still_needed = cost_after_discount - initial_money

    # FA
    answer = money_still_needed
    return answer