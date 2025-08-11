def solve():
    """Index: 4082.
    Returns: the number of water balloons Tom filled up.
    """
    # L1
    anthony_balloons = 44 # Anthony filled up 44 water balloons
    luke_fraction_denominator = 4 # one fourth as many balloons as Anthony
    luke_balloons = anthony_balloons / luke_fraction_denominator

    # L2
    tom_multiplier = 3 # Tom filled up 3 times as many
    tom_balloons = luke_balloons * tom_multiplier

    # FA
    answer = tom_balloons
    return answer