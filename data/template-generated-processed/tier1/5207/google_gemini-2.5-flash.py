def solve():
    """Index: 5207.
    Returns: the number of bills Geric had at the beginning.
    """
    # L1
    jessa_bills_left = 7 # Jessa has 7 bills left
    jessa_gave_to_geric = 3 # giving 3 bills to Geric
    jessa_initial_bills = jessa_bills_left + jessa_gave_to_geric

    # L2
    kyla_fewer_than_jessa = 2 # 2 fewer bills than Jessa
    kyla_bills = jessa_initial_bills - kyla_fewer_than_jessa

    # L3
    geric_multiplier = 2 # twice as many bills as Kyla
    geric_initial_bills = kyla_bills * geric_multiplier

    # FA
    answer = geric_initial_bills
    return answer