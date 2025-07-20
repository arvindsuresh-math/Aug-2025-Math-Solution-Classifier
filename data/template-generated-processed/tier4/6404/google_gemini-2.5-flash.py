from fractions import Fraction

def solve():
    """Index: 6404.
    Returns: the number of driveways Jimmy shoveled.
    """
    # L1
    num_candy_bars = 2 # 2 candy bars
    cost_per_candy_bar = 0.75 # $.75 each
    cost_candy_bars = num_candy_bars * cost_per_candy_bar

    # L2
    num_lollipops = 4 # 4 lollipops
    cost_per_lollipop = 0.25 # $.25 each
    cost_lollipops = num_lollipops * cost_per_lollipop

    # L3
    total_spent_candy = cost_candy_bars + cost_lollipops

    # L4
    fraction_spent = Fraction(1, 6) # 1/6 of the money he earned
    total_earned = total_spent_candy / fraction_spent

    # L5
    charge_per_driveway = 1.5 # $1.5 per driveway
    num_driveways = total_earned / charge_per_driveway

    # FA
    answer = num_driveways
    return answer