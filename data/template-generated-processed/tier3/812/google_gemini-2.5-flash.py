def solve():
    """Index: 812.
    Returns: the total number of pieces of candy caught by the friends.
    """
    # L1
    tabitha_candy = 22 # Tabitha caught 22 pieces of candy
    half_divisor = 2 # half the amount of candy as Tabitha caught
    julie_candy = tabitha_candy / half_divisor

    # L2
    stan_candy = 13 # Stan caught 13 pieces
    twice_multiplier = 2 # twice as much candy as Stan
    carlos_candy = twice_multiplier * stan_candy

    # L3
    total_candy = tabitha_candy + stan_candy + julie_candy + carlos_candy

    # FA
    answer = total_candy
    return answer