def solve():
    """Index: 2466.
    Returns: the number of legos Nellie has now.
    """
    # L1
    initial_legos = 380 # Nellie had 380 legos
    lost_legos = 57 # she lost 57 of them
    after_loss = initial_legos - lost_legos

    # L2
    given_to_sister = 24 # gave her sister 24 legos
    after_giving = after_loss - given_to_sister

    # FA
    answer = after_giving
    return answer