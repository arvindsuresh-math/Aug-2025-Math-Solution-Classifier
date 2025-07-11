from fractions import Fraction

def solve():
    """Index: 2217.
    Returns: the total amount Mrs. Taylor paid for the two televisions.
    """
    # L1
    cost_per_tv = 650 # cost $650 each
    number_of_tvs = 2 # two smart televisions
    total_cost_before_discount = cost_per_tv * number_of_tvs

    # L2
    discount_percentage = Fraction(25, 100) # 25% discount
    total_discount_amount = total_cost_before_discount * discount_percentage

    # L3
    final_price_paid = total_cost_before_discount - total_discount_amount

    # FA
    answer = final_price_paid
    return answer