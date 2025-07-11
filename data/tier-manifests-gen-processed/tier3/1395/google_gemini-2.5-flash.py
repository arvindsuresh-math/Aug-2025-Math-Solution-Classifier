from fractions import Fraction

def solve():
    """Index: 1395.
    Returns: the total amount Steve paid for the DVD.
    """
    # L1
    mike_paid = 5 # He paid $5 for it at the store
    twice_multiplier = 2 # twice as much
    online_movie_cost = twice_multiplier * mike_paid

    # L2
    shipping_percentage = Fraction(80, 100) # 80% of the price of the film he ordered
    shipping_costs = shipping_percentage * online_movie_cost

    # L3
    total_paid_by_steve = online_movie_cost + shipping_costs

    # FA
    answer = total_paid_by_steve
    return answer