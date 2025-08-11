from fractions import Fraction

def solve():
    """Index: 5190.
    Returns: the number of homes Kiaan still needs to distribute newspapers to.
    """
    # L1
    total_homes = 200 # 200 homes
    first_hour_fraction = Fraction(2, 5) # 2/5 of the homes
    homes_distributed_first_hour = first_hour_fraction * total_homes

    # L2
    remaining_homes_after_first_hour = total_homes - homes_distributed_first_hour

    # L3
    second_period_percentage = Fraction(60, 100) # 60 percent of the remaining homes
    homes_distributed_second_period = second_period_percentage * remaining_homes_after_first_hour

    # L4
    homes_still_need_distribution = remaining_homes_after_first_hour - homes_distributed_second_period

    # FA
    answer = homes_still_need_distribution
    return answer