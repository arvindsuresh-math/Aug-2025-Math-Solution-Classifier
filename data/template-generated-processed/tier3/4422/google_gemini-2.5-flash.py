from fractions import Fraction

def solve():
    """Index: 4422.
    Returns: the amount saved by buying collectively.
    """
    # L1
    num_iphones = 3 # buy three iPhones at once
    cost_per_iphone = 600 # an iPhone X costs $600
    total_cost_without_discount = num_iphones * cost_per_iphone

    # L2
    discount_percentage = Fraction(5, 100) # discount of 5% off
    amount_saved = discount_percentage * total_cost_without_discount

    # FA
    answer = amount_saved
    return answer