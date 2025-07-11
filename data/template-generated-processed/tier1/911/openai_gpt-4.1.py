def solve():
    """Index: 911.
    Returns: the combined time all the alligators walked.
    """
    # L1
    time_to_delta = 4 # 4 hours to walk from his home at the River Nile to the Nile Delta
    extra_time_return = 2 # 2 more hours than Paul took to walk to the Nile Delta
    time_return = time_to_delta + extra_time_return

    # L2
    total_time_paul = time_return + time_to_delta

    # L3
    other_alligators = 6 # Paul traveled with six other alligators
    time_each_other_alligator = time_return # each alligator traveled for six hours up the Nile to their home
    total_time_others = other_alligators * time_each_other_alligator

    # L4
    combined_time = total_time_paul + total_time_others

    # FA
    answer = combined_time
    return answer