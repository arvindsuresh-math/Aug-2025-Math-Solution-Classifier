def solve():
    """Index: 1123.
    Returns: the amount of money Evan still needs to buy the watch.
    """
    # L1
    evan_initial_money = 1 # Evan who has $1
    david_found_money = 12 # David found $12 on the street
    evan_total_money = evan_initial_money + david_found_money

    # L2
    watch_cost = 20 # buy a watch worth $20
    money_needed = watch_cost - evan_total_money

    # FA
    answer = money_needed
    return answer