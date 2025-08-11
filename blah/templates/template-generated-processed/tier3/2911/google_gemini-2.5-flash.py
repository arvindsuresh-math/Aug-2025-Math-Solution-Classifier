def solve():
    """Index: 2911.
    Returns: the number of granola bars each sister received.
    """
    # L1
    total_bars = 20 # a 20-pack of granola bars
    bars_kept_for_self = 7 # one for each day of the week
    bars_after_keeping = total_bars - bars_kept_for_self

    # L2
    traded_to_pete = 3 # traded three of the remaining bars
    bars_after_trading = bars_after_keeping - traded_to_pete

    # L3
    number_of_sisters = 2 # his two sisters
    bars_per_sister = bars_after_trading / number_of_sisters

    # FA
    answer = bars_per_sister
    return answer