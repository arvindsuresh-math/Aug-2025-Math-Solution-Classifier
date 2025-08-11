def solve():
    """Index: 372.
    Returns: the average time per kilometer.
    """
    # L1
    first_half_time = 20 # He ran the first half in 20 minutes
    second_half_time = 30 # He completed the second half in 30 minutes
    total_distance_km = 10 # TJ ran a 10K race
    total_time_minutes = first_half_time + second_half_time

    # L2
    average_time_per_km = total_time_minutes / total_distance_km

    # FA
    answer = average_time_per_km
    return answer