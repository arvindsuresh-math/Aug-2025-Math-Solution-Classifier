from fractions import Fraction

def solve():
    """Index: 4360.
    Returns: the total amount Ursula paid for her purchases.
    """
    # L1
    tea_cost = 10 # If the tea cost $10
    cheese_multiplier = 2 # twice the price of a package of cheese
    cheese_cost = tea_cost / cheese_multiplier

    # L2
    butter_percentage = Fraction(80, 100) # the price of the butter was 80% of the price of cheese
    butter_cost = butter_percentage * cheese_cost

    # L3
    bread_divisor = 2 # The bread was 2 times cheaper than the butter
    bread_cost = butter_cost / bread_divisor

    # L4
    total_cost = bread_cost + butter_cost + cheese_cost + tea_cost

    # FA
    answer = total_cost
    return answer