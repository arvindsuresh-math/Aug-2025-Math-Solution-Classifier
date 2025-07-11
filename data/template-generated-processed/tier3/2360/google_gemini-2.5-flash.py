from fractions import Fraction

def solve():
    """Index: 2360.
    Returns: the total amount Jaco will pay for the items.
    """
    # L1
    cost_per_pair_socks = 2 # 2 pairs of socks that cost $2 per pair
    num_pairs_socks = 2 # 2 pairs of socks
    cost_of_socks = cost_per_pair_socks * num_pairs_socks

    # L2
    shoes_cost = 74 # a pair of shoes for $74
    bag_cost = 42 # a bag that costs $42
    total_charge_before_discount = shoes_cost + cost_of_socks + bag_cost

    # L3
    discount_threshold = 100 # amount exceeding $100
    exceeding_amount = total_charge_before_discount - discount_threshold

    # L4
    discount_percentage = Fraction(10, 100) # 10% discount
    discount_amount = exceeding_amount * discount_percentage

    # L5
    final_payment = total_charge_before_discount - discount_amount

    # FA
    answer = final_payment
    return answer