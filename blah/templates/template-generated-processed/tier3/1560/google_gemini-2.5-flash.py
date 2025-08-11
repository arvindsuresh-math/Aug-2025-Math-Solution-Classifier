from fractions import Fraction

def solve():
    """Index: 1560.
    Returns: the amount of money Yvette remained with.
    """
    # L1
    percentage_increase = Fraction(20, 100) # 20% more expensive
    budget = 60 # budget of $60
    additional_cost = percentage_increase * budget

    # L2
    new_frame_price = budget + additional_cost

    # L3
    smaller_frame_fraction = Fraction(3, 4) # 3/4 the new price
    paid_price = smaller_frame_fraction * new_frame_price

    # L4
    money_remained = budget - paid_price

    # FA
    answer = money_remained
    return answer