def solve():
    """Index: 848.
    Returns: the number of cows on the farm.
    """
    # L1
    liters_per_group = 108 # 108 liters of milk per week
    cows_per_group = 6 # every 6 cows
    liters_per_cow_per_week = liters_per_group / cows_per_group

    # L2
    total_liters_produced = 2160 # 2160 liters of milk
    intermediate_cow_value = total_liters_produced / liters_per_cow_per_week

    # L3
    number_of_weeks = 5 # In five weeks
    actual_cows_on_farm = intermediate_cow_value / number_of_weeks

    # FA
    answer = actual_cows_on_farm
    return answer