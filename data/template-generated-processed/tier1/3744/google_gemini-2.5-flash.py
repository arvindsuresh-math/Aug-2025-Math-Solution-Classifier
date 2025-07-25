def solve():
    """Index: 3744.
    Returns: the amount of rum Don can still have.
    """
    # L1
    initial_rum_given = 10 # 10oz of rum
    max_multiplier = 3 # 3 times that amount
    max_rum_allowed = max_multiplier * initial_rum_given

    # L2
    rum_earlier = 12 # 12oz of rum earlier that day
    rum_consumed_total = initial_rum_given + rum_earlier

    # L3
    rum_can_still_have = max_rum_allowed - rum_consumed_total

    # FA
    answer = rum_can_still_have
    return answer