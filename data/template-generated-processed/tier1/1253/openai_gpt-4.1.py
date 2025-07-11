def solve():
    """Index: 1253.
    Returns: the total number of decorations Danai will put up in all.
    """
    # L1
    num_skulls = 12 # 12 plastic skulls
    num_broomsticks = 4 # 4 broomsticks
    num_spiderwebs = 12 # 12 spiderwebs
    num_cauldrons = 1 # a large cauldron
    initial_decorations = num_skulls + num_broomsticks + num_spiderwebs + num_cauldrons

    # L2
    multiplier_pumpkins = 2 # twice as many pumpkins
    num_pumpkins = num_spiderwebs * multiplier_pumpkins

    # L3
    budget_left = 20 # budget left to buy 20 more decorations
    left_to_put_up = 10 # has 10 left to put up
    answer = budget_left + left_to_put_up + initial_decorations + num_pumpkins
    return answer