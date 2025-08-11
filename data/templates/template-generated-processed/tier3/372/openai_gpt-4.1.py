def solve():
    """Index: 372.
    Returns: TJ's average time per kilometer in minutes.
    """
    # L1
    first_half_time = 20 # He ran the first half in 20 minutes
    second_half_time = 30 # He completed the second half in 30 minutes
    total_time = first_half_time + second_half_time

    # L2
    total_distance = 10 # 10K race (10 kilometers)
    avg_time_per_km = total_time / total_distance

    # FA
    answer = avg_time_per_km
    return answer