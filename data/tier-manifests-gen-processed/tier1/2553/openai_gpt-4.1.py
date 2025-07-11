def solve():
    """Index: 2553.
    Returns: the number of hours the puppy sleeps.
    """
    # L1
    connor_sleep = 6 # Connor sleeps 6 hours a night
    luke_more_than_connor = 2 # Luke sleeps 2 hours longer than Connor
    luke_sleep = luke_more_than_connor + connor_sleep

    # L2
    puppy_multiplier = 2 # puppy sleeps twice as long as Luke
    puppy_sleep = puppy_multiplier * luke_sleep

    # FA
    answer = puppy_sleep
    return answer