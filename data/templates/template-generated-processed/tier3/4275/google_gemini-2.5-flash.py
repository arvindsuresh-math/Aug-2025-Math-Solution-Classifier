def solve():
    """Index: 4275.
    Returns: the amount by which the three exceeded their goal.
    """
    # L1
    ken_funds = 600 # Ken has $600
    mary_multiplier = 5 # Mary’s collection is five times what Ken has
    mary_funds = mary_multiplier * ken_funds

    # L2
    scott_divisor = 3 # three times Scott’s funds
    scott_funds = mary_funds / scott_divisor

    # L3
    total_raised = mary_funds + scott_funds + ken_funds

    # L4
    goal_amount = 4000 # raising $4,000 for their local children’s cancer hospital
    exceeded_goal_by = total_raised - goal_amount

    # FA
    answer = exceeded_goal_by
    return answer