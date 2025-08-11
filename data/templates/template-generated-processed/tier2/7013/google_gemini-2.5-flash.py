def solve():
    """Index: 7013.
    Returns: the size of the bucket in ounces.
    """
    # L1
    leak_rate = 1.5 # rate of 1.5 ounces per hour
    leak_duration = 12 # as long as 12 hours
    leaked_volume = leak_rate * leak_duration

    # L2
    twice_factor = 2 # twice the amount of fluid
    bucket_size = leaked_volume * twice_factor

    # FA
    answer = bucket_size
    return answer