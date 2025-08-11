def solve():
    """Index: 5798.
    Returns: the number of apples Lex will have left to eat raw.
    """
    # L1
    total_apples = 85 # He picked 85 apples.
    worm_fraction_denominator = 5 # a fifth of the apples have worms
    wormy_apples = total_apples / worm_fraction_denominator

    # L2
    additional_bruised_apples = 9 # nine more than one fifth are bruised
    bruised_apples = wormy_apples + additional_bruised_apples

    # L3
    apples_to_eat_raw = total_apples - bruised_apples - wormy_apples

    # FA
    answer = apples_to_eat_raw
    return answer