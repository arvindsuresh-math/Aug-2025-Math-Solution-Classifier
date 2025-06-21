def solve(
        assignment_time: int = 10, # 10 minutes to complete
        total_sticky_keys: int = 15, # 15 keys that are sticky
        time_per_key: int = 3, # 3 minutes to clean one
        keys_left_to_clean: int = 14 # there are 14 left to clean
    ):
    """Index: 636.
    Returns: the total minutes needed to clean the remaining keys and finish the assignment.
    """
    #: L1
    time_to_clean_remaining_keys = keys_left_to_clean * time_per_key

    #: L2
    total_time_needed = time_to_clean_remaining_keys + assignment_time

    answer = total_time_needed # FINAL ANSWER
    return answer