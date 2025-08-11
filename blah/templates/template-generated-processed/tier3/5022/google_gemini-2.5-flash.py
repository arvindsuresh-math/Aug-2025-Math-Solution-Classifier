def solve():
    """Index: 5022.
    Returns: the total yards Georgie will be able to run within 10 seconds.
    """
    # L1
    initial_yards = 40 # 40 yards
    improvement_percentage_numerator = 40 # forty percent
    percentage_denominator = 100 # WK
    additional_yards = initial_yards * improvement_percentage_numerator / percentage_denominator

    # L2
    improved_yards_in_5_seconds = initial_yards + additional_yards

    # L3
    target_time_seconds = 10 # within 10 seconds
    initial_time_seconds = 5 # within 5 seconds
    time_multiplier = target_time_seconds / initial_time_seconds
    total_yards_in_10_seconds = improved_yards_in_5_seconds * time_multiplier

    # FA
    answer = total_yards_in_10_seconds
    return answer