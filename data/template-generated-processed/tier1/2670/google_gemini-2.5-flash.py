def solve():
    """Index: 2670.
    Returns: the total number of people counted on the two days.
    """
    # L1
    multiplier_first_day = 2 # twice the total number
    people_second_day = 500 # 500 people were counted on the second day
    people_first_day = multiplier_first_day * people_second_day

    # L2
    total_people = people_first_day + people_second_day

    # FA
    answer = total_people
    return answer