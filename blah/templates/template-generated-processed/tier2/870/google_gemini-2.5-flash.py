def solve():
    """Index: 870.
    Returns: the total time it took Matthew to make the cakes on that day.
    """
    # L1
    usual_bake_time = 1.5 # 1.5 hours to bake the cakes
    twice_factor = 2 # took twice as long
    actual_bake_time = twice_factor * usual_bake_time

    # L2
    assemble_time = 1 # 1 hour to assemble ingredients
    decorate_time = 1 # 1 hour to decorate each cake
    total_time = assemble_time + actual_bake_time + decorate_time

    # FA
    answer = total_time
    return answer