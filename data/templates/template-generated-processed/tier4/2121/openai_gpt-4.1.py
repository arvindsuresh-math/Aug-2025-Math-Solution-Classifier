def solve():
    """Index: 2121.
    Returns: the dollar amount more per batch to make almond butter cookies instead of peanut butter cookies.
    """
    # L1
    pb_jar_cost = 3 # A jar of peanut butter costs $3
    ab_pb_cost_ratio = 3 # almond butter costs three times the amount
    ab_jar_cost = ab_pb_cost_ratio * pb_jar_cost

    # L2
    jar_per_batch = 0.5 # It takes half a jar to make a batch
    ab_batch_cost = ab_jar_cost / jar_per_batch

    # L3
    pb_batch_cost = pb_jar_cost / jar_per_batch

    # L4
    batch_cost_difference = ab_batch_cost - pb_batch_cost

    # FA
    answer = batch_cost_difference
    return answer