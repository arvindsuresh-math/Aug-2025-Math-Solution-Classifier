from fractions import Fraction

def solve():
    """Index: 1942.
    Returns: the amount saved by buying 3 pairs at once with a discount.
    """
    # L1
    cost_per_pair = 10 # Each pair normally cost $10
    num_pairs = 3 # 3 or more pairs
    cost_without_discount = num_pairs * cost_per_pair

    # L2
    discount_percentage_numerator = 10 # discount of 10%
    discount_percentage_denominator = 100 # discount of 10%
    discount_percentage = Fraction(discount_percentage_numerator, discount_percentage_denominator)
    cost_with_discount = cost_without_discount - (cost_without_discount * discount_percentage)

    # L3
    savings = cost_without_discount - cost_with_discount

    # FA
    answer = savings
    return answer