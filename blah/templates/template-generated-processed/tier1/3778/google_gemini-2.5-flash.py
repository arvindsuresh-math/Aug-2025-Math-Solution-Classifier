def solve():
    """Index: 3778.
    Returns: the number of miles still needed to be added to the highway.
    """
    # L1
    final_length = 650 # up to 650 miles
    current_length = 200 # current length of 200 miles
    miles_to_construct = final_length - current_length

    # L2
    built_first_day = 50 # 50 miles are built on the first day
    remaining_after_day1 = miles_to_construct - built_first_day

    # L3
    multiplier_second_day = 3 # three times this amount
    built_second_day = built_first_day * multiplier_second_day

    # L4
    miles_still_needed = remaining_after_day1 - built_second_day

    # FA
    answer = miles_still_needed
    return answer