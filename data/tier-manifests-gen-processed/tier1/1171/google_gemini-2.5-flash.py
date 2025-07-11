def solve():
    """Index: 1171.
    Returns: the total number of trophies Jack and Michael will have altogether after three years.
    """
    # L1
    michael_trophies_now = 30 # Michael has 30 trophies right now
    michael_increase_in_three_years = 100 # number of his trophies increases by 100 in three years
    michael_trophies_after_three_years = michael_trophies_now + michael_increase_in_three_years

    # L2
    jack_multiplier = 10 # ten times more handball trophies
    jack_trophies_after_three_years = jack_multiplier * michael_trophies_now

    # L3
    total_trophies = jack_trophies_after_three_years + michael_trophies_after_three_years

    # FA
    answer = total_trophies
    return answer