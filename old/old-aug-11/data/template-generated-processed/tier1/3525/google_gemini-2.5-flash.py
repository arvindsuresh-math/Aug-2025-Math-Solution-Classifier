def solve():
    """Index: 3525.
    Returns: the number of tattoos Adam has.
    """
    # L1
    tattoos_per_arm = 2 # two tattoos on each of his arms
    num_arms = 2 # WK
    tattoos_on_arms = num_arms * tattoos_per_arm

    # L2
    tattoos_per_leg = 3 # three tattoos on each of his legs
    num_legs = 2 # WK
    tattoos_on_legs = num_legs * tattoos_per_leg

    # L3
    jason_tattoos = tattoos_on_arms + tattoos_on_legs

    # L4
    multiplier_twice = 2 # twice as many tattoos
    twice_jason_tattoos = multiplier_twice * jason_tattoos

    # L5
    adam_more_than_twice = 3 # three more than twice as many tattoos
    adam_tattoos = adam_more_than_twice + twice_jason_tattoos

    # FA
    answer = adam_tattoos
    return answer