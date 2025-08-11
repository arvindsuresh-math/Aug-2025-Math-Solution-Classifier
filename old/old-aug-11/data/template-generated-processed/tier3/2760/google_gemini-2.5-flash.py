def solve():
    """Index: 2760.
    Returns: Joel's age when his dad is twice as old as him.
    """
    # L1
    dad_current_age = 32 # his dad is 32 years old
    joel_current_age = 5 # Joel is 5 years old
    age_difference = dad_current_age - joel_current_age

    # L2
    double_factor = 2 # twice as old as him
    dad_future_age = age_difference * double_factor

    # L3
    joel_future_age = dad_future_age / double_factor

    # FA
    answer = joel_future_age
    return answer