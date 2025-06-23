def solve(
    total_keys: int = 15,  # she counts 15 keys that are sticky
    time_per_key: int = 3,  # it takes 3 minutes to clean one key
    time_assignment: int = 10  # assignment will only take 10 minutes to complete
):
    """Index: 636.
    Returns: the total minutes needed to clean the remaining keys and finish the assignment.
    """
    #: L1
    keys_left = total_keys - 1
    cleaning_time = keys_left * time_per_key

    #: L2
    total_time = cleaning_time + time_assignment

    answer = total_time  # FINAL ANSWER
    return answer