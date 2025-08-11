def solve():
    """Index: 1777.
    Returns: the total number of basketballs donated.
    """
    # L1
    total_pool_floats = 120 # 120 pool floats were donated
    damaged_fraction_denominator = 4 # a quarter of these were damaged
    discarded_pool_floats = total_pool_floats / damaged_fraction_denominator

    # L2
    remaining_pool_floats = total_pool_floats - discarded_pool_floats

    # L3
    basketball_hoops = 60 # 60 of these were basketball hoops
    footballs = 50 # 50 footballs
    tennis_balls = 40 # 40 tennis balls
    non_basketball_donations = basketball_hoops + remaining_pool_floats + footballs + tennis_balls

    # L4
    total_donations = 300 # 300 donations to organize
    initial_basketballs = total_donations - non_basketball_donations

    # L5
    hoops_with_balls_divisor = 2 # half of which also had basketballs included
    basketballs_from_hoops = basketball_hoops / hoops_with_balls_divisor

    # L6
    total_basketballs_donated = initial_basketballs + basketballs_from_hoops

    # FA
    answer = total_basketballs_donated
    return answer