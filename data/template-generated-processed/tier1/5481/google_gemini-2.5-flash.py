def solve():
    """Index: 5481.
    Returns: the total number of pastries that the four have.
    """
    # L1
    grace_pastries = 30 # Grace has 30 pastries
    calvin_phoebe_less_than_grace = 5 # five less than Grace
    calvin_phoebe_pastries_each = grace_pastries - calvin_phoebe_less_than_grace

    # L2
    phoebe_calvin_total = calvin_phoebe_pastries_each + calvin_phoebe_pastries_each

    # L3
    phoebe_calvin_grace_total = phoebe_calvin_total + grace_pastries

    # L4
    calvin_phoebe_more_than_frank = 8 # 8 more pastries than Frank
    frank_pastries = calvin_phoebe_pastries_each - calvin_phoebe_more_than_frank

    # L5
    total_pastries = frank_pastries + phoebe_calvin_grace_total

    # FA
    answer = total_pastries
    return answer