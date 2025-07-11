def solve():
    """Index: 2963.
    Returns: Tully's age a year ago.
    """
    # L1
    kate_now = 29 # Kate is now 29 years old
    years_from_now = 3 # Three years from now
    kate_future = kate_now + years_from_now

    # L2
    tully_multiplier = 2 # twice as old as Kate
    tully_future = kate_future * tully_multiplier

    # L3
    tully_now = tully_future - years_from_now

    # L4
    years_ago = 1 # a year ago
    tully_last_year = tully_now - years_ago

    # FA
    answer = tully_last_year
    return answer