def solve():
    """Index: 1475.
    Returns: the total number of marbles Pete has after trading.
    """
    # L1
    total_marbles = 10 # a bag with 10 marbles
    blue_percent_decimal = 0.4 # 40% are blue
    initial_blue_marbles = total_marbles * blue_percent_decimal

    # L2
    total_percent = 100 # WK
    blue_percent_num = 40 # 40% are blue
    red_percent_num = total_percent - blue_percent_num

    # L3
    red_percent_decimal = 0.6 # 60% of the marbles are red
    initial_red_marbles = total_marbles * red_percent_decimal

    # L4
    kept_red_marble = 1 # keeps 1 red marble
    traded_red_marbles = initial_red_marbles - kept_red_marble

    # L5
    trade_ratio_blue = 2 # two blue marbles for every red one
    new_blue_marbles = traded_red_marbles * trade_ratio_blue

    # L6
    total_marbles_after_trade = initial_blue_marbles + kept_red_marble + new_blue_marbles

    # FA
    answer = total_marbles_after_trade
    return answer