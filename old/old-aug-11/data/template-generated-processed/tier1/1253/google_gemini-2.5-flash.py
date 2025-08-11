def solve():
    """Index: 1253.
    Returns: the total number of decorations Danai will put up.
    """
    # L1
    skulls = 12 # 12 plastic skulls
    broomsticks = 4 # 4 broomsticks
    spiderwebs = 12 # 12 spiderwebs
    cauldron = 1 # a large cauldron
    initial_decorations = skulls + broomsticks + spiderwebs + cauldron

    # L2
    multiplier_for_twice = 2 # twice as many pumpkins
    pumpkins = spiderwebs * multiplier_for_twice

    # L3
    budget_decorations = 20 # 20 more decorations
    left_to_put_up = 10 # 10 left to put up
    total_decorations = budget_decorations + left_to_put_up + initial_decorations + pumpkins

    # FA
    answer = total_decorations
    return answer