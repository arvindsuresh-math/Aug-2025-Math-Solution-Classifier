def solve():
    """Index: 6681.
    Returns: the total time Matt spends cleaning his car.
    """
    # L1
    outside_wash_time = 80 # Matt spends 80 minutes washing the outside of his car
    inside_time_divisor = 4 # 1/4 that amount of time
    inside_wash_time = outside_wash_time / inside_time_divisor

    # L2
    total_cleaning_time = inside_wash_time + outside_wash_time

    # FA
    answer = total_cleaning_time
    return answer