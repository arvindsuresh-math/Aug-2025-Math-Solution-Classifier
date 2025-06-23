def solve(
    assignment_time: int = 10, # assignment will only take 10 minutes to complete
    total_sticky_keys: int = 15, # She counts 15 keys that are sticky
    time_per_key: int = 3, # times it to take 3 minutes to clean one
    keys_left_after_one: int = 14 # After Tina has cleaned one key, there are 14 left to clean
):
    """Index: 636.
    Returns: the total time in minutes needed to clean the remaining keys and finish the assignment.
    """
    #: L1
    cleaning_time_remaining = keys_left_after_one * time_per_key

    #: L2
    total_time_needed = cleaning_time_remaining + assignment_time

    answer = total_time_needed # FINAL ANSWER
    return answer