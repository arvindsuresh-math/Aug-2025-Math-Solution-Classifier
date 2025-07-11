def solve():
    """Index: 1303.
    Returns: the total amount Terry spent.
    """
    # L1
    monday_cost = 6 # 6$ for breakfast on Monday
    
    # L2
    twice_multiplier = 2 # twice as much on Tuesday
    tuesday_cost = monday_cost * twice_multiplier

    # L3
    double_multiplier = 2 # double what he did the previous two days combined
    wednesday_cost = double_multiplier * (monday_cost + tuesday_cost)

    # L4
    total_cost = monday_cost + tuesday_cost + wednesday_cost

    # FA
    answer = total_cost
    return answer