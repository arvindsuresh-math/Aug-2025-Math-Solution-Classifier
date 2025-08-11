def solve():
    """Index: 870.
    Returns: the total time in hours it took Matthew to make his cakes on the day the oven failed.
    """
    # L1
    bake_time_usual = 1.5 # usually takes 1.5 hours to bake the cakes
    bake_time_multiplier = 2 # took twice as long
    bake_time_failed = bake_time_multiplier * bake_time_usual

    # L2
    assemble_time = 1 # takes 1 hour to assemble ingredients
    decorate_time = 1 # another 1 hour to decorate each cake
    total_time = assemble_time + bake_time_failed + decorate_time

    # FA
    answer = total_time
    return answer