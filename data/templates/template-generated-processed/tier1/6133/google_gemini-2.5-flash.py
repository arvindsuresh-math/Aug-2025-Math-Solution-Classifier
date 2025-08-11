def solve():
    """Index: 6133.
    Returns: the total number of toys they all have.
    """
    # L1
    jaxon_toys = 15 # Jaxon got 15 toys

    # L2
    multiplier_twice = 2 # twice as many toys
    gabriel_toys = multiplier_twice * jaxon_toys

    # L3
    jerry_more_than_gabriel = 8 # 8 more toys than Gabriel
    jerry_toys = gabriel_toys + jerry_more_than_gabriel

    # L4
    total_toys = jaxon_toys + gabriel_toys + jerry_toys

    # FA
    answer = total_toys
    return answer