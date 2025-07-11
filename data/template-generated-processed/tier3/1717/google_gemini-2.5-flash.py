from fractions import Fraction

def solve():
    """Index: 1717.
    Returns: the total cost a customer will pay for 3 pairs of jeans.
    """
    # L1
    price_per_pair = 40 # for $40
    num_pairs_for_base_cost = 2 # every two pairs of jeans
    cost_two_pairs_initial = price_per_pair * num_pairs_for_base_cost

    # L2
    discount_percentage = Fraction(10, 100) # 10% discount
    discount_amount = cost_two_pairs_initial * discount_percentage

    # L3
    cost_two_pairs_after_discount = cost_two_pairs_initial - discount_amount

    # L4
    price_for_third_pair = 40 # for $40
    total_cost_three_pairs = cost_two_pairs_after_discount + price_for_third_pair

    # FA
    answer = total_cost_three_pairs
    return answer