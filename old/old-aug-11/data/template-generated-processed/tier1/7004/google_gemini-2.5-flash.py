def solve():
    """Index: 7004.
    Returns: the total number of jokes told by Jessy and Alan over two Saturdays.
    """
    # L1
    jessy_jokes_past_saturday = 11 # eleven jokes this past Saturday
    alan_jokes_past_saturday = 7 # seven jokes
    total_jokes_past_saturday = jessy_jokes_past_saturday + alan_jokes_past_saturday

    # L2
    doubling_factor = 2 # doubled the number of jokes
    jessy_jokes_next_saturday = doubling_factor * jessy_jokes_past_saturday

    # L3
    alan_jokes_next_saturday = doubling_factor * alan_jokes_past_saturday

    # L4
    total_jokes_next_saturday = alan_jokes_next_saturday + jessy_jokes_next_saturday

    # L5
    total_jokes_overall = total_jokes_next_saturday + total_jokes_past_saturday

    # FA
    answer = total_jokes_overall
    return answer