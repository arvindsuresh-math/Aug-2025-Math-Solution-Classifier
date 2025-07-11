def solve():
    """Index: 2553.
    Returns: the duration the puppy sleeps.
    """
    # L1
    luke_longer_than_connor = 2 # 2 hours longer than Connor
    connor_sleep_hours = 6 # Connor sleeps 6 hours a night
    luke_sleep_hours = luke_longer_than_connor + connor_sleep_hours

    # L2
    puppy_sleep_multiplier = 2 # twice as long as Luke
    puppy_sleep_hours = puppy_sleep_multiplier * luke_sleep_hours

    # FA
    answer = puppy_sleep_hours
    return answer