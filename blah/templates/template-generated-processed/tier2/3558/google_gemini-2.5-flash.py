def solve():
    """Index: 3558.
    Returns: the number of knockouts Rocky had in the first round.
    """
    # L1
    total_fights = 190 # 190 fights
    knockout_percentage_decimal = 0.50 # 50 percent of his fights
    total_knockouts = total_fights * knockout_percentage_decimal

    # L2
    first_round_knockout_percentage_decimal = 0.2 # 20 percent of the knockouts
    first_round_knockouts = total_knockouts * first_round_knockout_percentage_decimal

    # FA
    answer = first_round_knockouts
    return answer