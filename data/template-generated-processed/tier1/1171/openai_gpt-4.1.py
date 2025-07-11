def solve():
    """Index: 1171.
    Returns: the total number of trophies Jack and Michael will have altogether after three years.
    """
    # L1
    michael_now = 30 # Michael has 30 trophies right now
    michael_increase = 100 # increases by 100 in three years
    michael_future = michael_now + michael_increase

    # L2
    jack_multiplier = 10 # ten times more handball trophies than Michael has right now
    jack_future = jack_multiplier * michael_now

    # L3
    total_trophies = jack_future + michael_future

    # FA
    answer = total_trophies
    return answer