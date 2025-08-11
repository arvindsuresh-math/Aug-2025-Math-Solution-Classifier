def solve():
    """Index: 6778.
    Returns: the total number of pills Joey will take in a week.
    """
    # L1
    pills_day1 = 1 # take one pill
    increase_per_day = 2 # take two more pills than the previous day
    pills_day2 = pills_day1 + increase_per_day

    # L2
    pills_day3 = pills_day2 + increase_per_day

    # L3
    pills_day4 = pills_day3 + increase_per_day

    # L4
    pills_day5 = pills_day4 + increase_per_day

    # L5
    pills_day6 = pills_day5 + increase_per_day

    # L6
    pills_day7 = pills_day6 + increase_per_day

    # L7
    total_pills_week = pills_day1 + pills_day2 + pills_day3 + pills_day4 + pills_day5 + pills_day6 + pills_day7

    # FA
    answer = total_pills_week
    return answer