def solve():
    """Index: 262.
    Returns: the number of times Jack's current number of apples could fit into Jill's basket.
    """
    # L1
    jack_basket_capacity = 12 # Jack's basket is full when it has 12 apples
    jill_capacity_multiplier = 2 # Jill's basket can hold twice as much as Jack's basket
    jill_basket_capacity = jack_basket_capacity * jill_capacity_multiplier

    # L2
    jack_space_left = 4 # currently space for 4 more
    jack_current_apples = jack_basket_capacity - jack_space_left

    # L3
    times_jack_apples_fit_in_jill = jill_basket_capacity / jack_current_apples

    # FA
    answer = times_jack_apples_fit_in_jill
    return answer