def solve():
    """Index: 636.
    Returns: the total minutes needed to clean remaining keys and finish the assignment.
    """
    # L1
    remaining_keys_to_clean = 14 # After Tina has cleaned one key, there are 14 left to clean.
    time_per_key = 3 # times it to take 3 minutes to clean one.
    time_to_clean_keys = remaining_keys_to_clean * time_per_key

    # L2
    assignment_time = 10 # her assignment will only take 10 minutes to complete.
    total_time_needed = time_to_clean_keys + assignment_time

    # FA
    answer = total_time_needed
    return answer