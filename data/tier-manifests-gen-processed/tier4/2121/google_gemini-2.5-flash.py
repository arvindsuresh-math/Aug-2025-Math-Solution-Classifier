def solve():
    """Index: 2121.
    Returns: the additional cost per batch for almond butter cookies.
    """
    # L1
    pb_jar_cost = 3 # A jar of peanut butter costs $3
    almond_butter_cost_factor = 3 # three times the amount that a jar of peanut butter does
    almond_butter_jar_cost = almond_butter_cost_factor * pb_jar_cost

    # L2
    jar_fraction_for_batch_divisor = 2 # half a jar
    almond_butter_batch_cost = almond_butter_jar_cost / jar_fraction_for_batch_divisor

    # L3
    pb_batch_cost = pb_jar_cost / jar_fraction_for_batch_divisor

    # L4
    cost_difference = almond_butter_batch_cost - pb_batch_cost

    # FA
    answer = cost_difference
    return answer