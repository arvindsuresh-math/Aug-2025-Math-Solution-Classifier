def solve():
    """Index: 1303.
    Returns: the total amount Terry spent over the three days.
    """
    # L1
    monday_spent = 6 # Terry spent 6$ for breakfast on Monday

    # L2
    tuesday_multiplier = 2 # twice as much on Tuesday
    tuesday_spent = monday_spent * tuesday_multiplier

    # L3
    wednesday_multiplier = 2 # double what he did the previous two days combined
    wednesday_spent = wednesday_multiplier * (monday_spent + tuesday_spent)

    # L4
    total_spent = monday_spent + tuesday_spent + wednesday_spent

    # FA
    answer = total_spent
    return answer