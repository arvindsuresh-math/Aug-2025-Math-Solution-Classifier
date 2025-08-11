from fractions import Fraction

def solve():
    """Index: 1130.
    Returns: the number of additional packages Max could deliver.
    """
    # L1
    maximum_daily_packages = 35 # a maximum of 35 packages
    working_days_per_week = 7 # WK
    max_weekly_capacity = maximum_daily_packages * working_days_per_week

    # L2
    days_at_max_performance = 2 # only twice
    packages_delivered_at_max_performance = days_at_max_performance * maximum_daily_packages

    # L3
    fraction_one_seventh = Fraction(1, 7) # only one-seventh of the maximum possible daily performance
    packages_delivered_one_seventh = fraction_one_seventh * maximum_daily_packages

    # L4
    fraction_four_fifth = Fraction(4, 5) # only fourth-fifth of the maximum daily performance
    packages_delivered_four_fifth = fraction_four_fifth * maximum_daily_packages

    # L5
    packages_unloaded_other_two_days = 50 # On two other days, Max unloaded a total of 50 packages
    remaining_capacity = max_weekly_capacity - packages_delivered_four_fifth - packages_delivered_one_seventh - packages_delivered_at_max_performance - packages_unloaded_other_two_days

    # FA
    answer = remaining_capacity
    return answer