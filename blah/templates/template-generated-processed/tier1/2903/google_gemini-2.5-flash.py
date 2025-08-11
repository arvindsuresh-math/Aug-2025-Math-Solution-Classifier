def solve():
    """Index: 2903.
    Returns: the age difference between Lexie's brother and her sister.
    """
    # L1
    lexie_age = 8 # If Lexie is 8
    lexie_older_than_brother = 6 # Lexie is 6 years older than her brother
    brother_age = lexie_age - lexie_older_than_brother

    # L2
    sister_multiplier = 2 # sister is twice her age
    sister_age = lexie_age * sister_multiplier

    # L3
    age_difference = sister_age - brother_age

    # FA
    answer = age_difference
    return answer