def solve():
    """Index: 4008.
    Returns: the number of instances of bullying Kris is responsible for.
    """
    # L1
    multiplier = 3 # three times as many days
    fingers_and_toes_count = 20 # WK
    total_suspended_days = multiplier * fingers_and_toes_count

    # L2
    days_per_instance = 3 # suspended for 3 days
    instances_of_bullying = total_suspended_days / days_per_instance

    # FA
    answer = instances_of_bullying
    return answer