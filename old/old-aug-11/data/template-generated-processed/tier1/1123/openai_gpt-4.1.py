def solve():
    """Index: 1123.
    Returns: the amount Evan still needs to buy the watch.
    """
    # L1
    evan_initial = 1 # Evan who has $1
    david_found = 12 # David found $12
    evan_total = evan_initial + david_found

    # L2
    watch_price = 20 # watch worth $20
    evan_still_needs = watch_price - evan_total

    # FA
    answer = evan_still_needs
    return answer