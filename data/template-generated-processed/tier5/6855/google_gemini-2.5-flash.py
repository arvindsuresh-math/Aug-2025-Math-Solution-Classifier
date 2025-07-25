def solve():
    """Index: 6855.
    Returns: the number of hours it will take Cordelia to bleach her hair.
    """
    # L4
    total_process_hours = 9 # The whole process will take 9 hours
    dyeing_multiplier = 2 # Dyeing takes twice as long as bleaching
    bleaching_coefficient = 1 # WK
    total_coefficient = bleaching_coefficient + dyeing_multiplier
    
    bleaching_hours = total_process_hours / total_coefficient

    # FA
    answer = bleaching_hours
    return answer