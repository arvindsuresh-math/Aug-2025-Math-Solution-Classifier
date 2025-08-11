def solve():
    """Index: 1578.
    Returns: the amount of money Manny will have left.
    """
    # L1
    total_cost_five_chairs = 55 # Five plastic chairs cost $55
    num_chairs_five = 5 # Five plastic chairs cost $55
    cost_per_chair = total_cost_five_chairs / num_chairs_five

    # L2
    num_chairs_to_buy = 2 # two chairs
    cost_two_chairs = cost_per_chair * num_chairs_to_buy

    # L3
    num_chairs_for_table = 3 # Three plastic chairs cost as much as a portable table
    cost_portable_table = cost_per_chair * num_chairs_for_table

    # L4
    total_cost_manny = cost_two_chairs + cost_portable_table

    # L5
    initial_money = 100 # his $100
    money_left = initial_money - total_cost_manny

    # FA
    answer = money_left
    return answer