def solve():
    """Index: 2466.
    Returns: the number of legos Nellie has now.
    """
    # L1
    initial_legos = 380 # Nellie had 380 legos
    lost_legos = 57 # lost 57 of them
    after_losing_legos = initial_legos - lost_legos

    # L2
    given_to_sister_legos = 24 # gave her sister 24 legos
    remaining_legos = after_losing_legos - given_to_sister_legos

    # FA
    answer = remaining_legos
    return answer