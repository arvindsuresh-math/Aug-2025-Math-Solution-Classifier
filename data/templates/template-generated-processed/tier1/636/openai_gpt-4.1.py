def solve():
    """Index: 636.
    Returns: the total minutes Tina needs to clean the remaining keys and finish her assignment.
    """
    # L1
    keys_left = 14 # there are 14 left to clean
    minutes_per_key = 3 # 3 minutes to clean one
    cleaning_time = keys_left * minutes_per_key

    # L2
    assignment_time = 10 # assignment will only take 10 minutes
    total_time = cleaning_time + assignment_time

    # FA
    answer = total_time
    return answer