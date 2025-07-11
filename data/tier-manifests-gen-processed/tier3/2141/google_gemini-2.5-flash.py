from fractions import Fraction

def solve():
    """Index: 2141.
    Returns: the total time Jerry mows each week.
    """
    # L1
    total_acres_mowed_weekly = 8 # 8 acres of lawn each week
    riding_mower_fraction = Fraction(3, 4) # ¾ of it
    acres_mowed_riding_mower = total_acres_mowed_weekly * riding_mower_fraction

    # L2
    riding_mower_speed = 2 # can cut 2 acres an hour
    time_riding_mower = acres_mowed_riding_mower / riding_mower_speed

    # L3
    acres_mowed_push_mower = total_acres_mowed_weekly - acres_mowed_riding_mower

    # L4
    push_mower_time_per_acre = 1 # can cut 1 acre an hour
    time_push_mower = acres_mowed_push_mower * push_mower_time_per_acre

    # L5
    total_mowing_time = time_riding_mower + time_push_mower

    # FA
    answer = total_mowing_time
    return answer