from fractions import Fraction

def solve():
    """Index: 488.
    Returns: the additional amount of money Mrs. Smith will still need after the discount.
    """
    # L1
    two_fifths = Fraction(2, 5) # two-fifths more money than she had
    initial_money = 500 # $500
    extra_needed = two_fifths * initial_money

    # L2
    total_needed = extra_needed + initial_money

    # L3
    discount_percent = Fraction(15, 100) # 15% discount
    discount_amount = discount_percent * total_needed

    # L4
    discounted_price = total_needed - discount_amount

    # L5
    answer = discounted_price - initial_money
    return answer