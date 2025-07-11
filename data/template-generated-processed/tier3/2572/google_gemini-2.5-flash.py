def solve():
    """Index: 2572.
    Returns: the length of Derrick's yard.
    """
    # L1
    brianne_yard_length = 30 # Brianne's yard is 30 yards long
    brianne_alex_multiplier = 6 # Brianne's yard is 6 times the size of Alex's
    alex_yard_length = brianne_yard_length / brianne_alex_multiplier

    # L2
    derrick_alex_multiplier = 2 # half the size of Derrick's (meaning Derrick's is twice Alex's)
    derrick_yard_length = alex_yard_length * derrick_alex_multiplier

    # FA
    answer = derrick_yard_length
    return answer