from fractions import Fraction

def solve():
    """Index: 1407.
    Returns: the total amount Nina paid for both pairs of shoes.
    """
    # L1
    first_pair_price = 22 # bought one of them for $22
    percentage_more_expensive = Fraction(50, 100) # 50% more expensive
    more_expensive_amount = percentage_more_expensive * first_pair_price

    # L2
    second_pair_price = first_pair_price + more_expensive_amount

    # L3
    total_paid = second_pair_price + first_pair_price

    # FA
    answer = total_paid
    return answer