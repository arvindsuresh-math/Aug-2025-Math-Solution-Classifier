def solve():
    """Index: 886.
    Returns: the amount of money Jack has remaining after his purchases.
    """
    # L1
    initial_bottles = 4 # bought 4 bottles of water
    mother_multiplier = 2 # buy twice as many bottles as he already bought
    bottles_mother_requested = mother_multiplier * initial_bottles

    # L2
    total_bottles = initial_bottles + bottles_mother_requested

    # L3
    bottle_cost = 2 # Each bottle cost $2
    total_water_cost = total_bottles * bottle_cost

    # L4
    cheese_pounds = 0.5 # half a pound of cheese
    cheese_cost_per_pound = 10 # 1 pound of cheese costs $10
    cheese_cost = cheese_pounds * cheese_cost_per_pound

    # L5
    total_spent = total_water_cost + cheese_cost

    # L6
    initial_money = 100 # Jack went to a supermarket with $100
    money_remaining = initial_money - total_spent

    # FA
    answer = money_remaining
    return answer