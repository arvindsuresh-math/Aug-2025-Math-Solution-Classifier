def solve():
    """Index: 886.
    Returns: the amount of money Jack has remaining.
    """
    # L1
    initial_bottles_bought = 4 # bought 4 bottles of water
    multiplier_twice = 2 # twice as many bottles
    bottles_mother_asked = multiplier_twice * initial_bottles_bought

    # L2
    total_bottles_bought = initial_bottles_bought + bottles_mother_asked

    # L3
    cost_per_bottle = 2 # Each bottle cost $2
    total_cost_water = total_bottles_bought * cost_per_bottle

    # L4
    cheese_amount_pounds = 0.5 # half a pound of cheese
    cost_per_pound_cheese = 10 # 1 pound of cheese costs $10
    total_cost_cheese = cheese_amount_pounds * cost_per_pound_cheese

    # L5
    total_spent = total_cost_water + total_cost_cheese

    # L6
    initial_money = 100 # with $100
    money_remaining = initial_money - total_spent

    # FA
    answer = money_remaining
    return answer