def solve():
    """Index: 3083.
    Returns: the total amount Alvin earns from selling his marble set.
    """
    # L1
    total_marbles = 100 # He has 100 marbles
    white_percent_decimal = 0.2 # 20% are white
    num_white_marbles = total_marbles * white_percent_decimal

    # L2
    black_percent_decimal = 0.3 # 30% are black
    num_black_marbles = total_marbles * black_percent_decimal

    # L3
    num_color_marbles = total_marbles - num_white_marbles - num_black_marbles

    # L4
    white_marble_price = 0.05 # for a nickel each
    earnings_white = num_white_marbles * white_marble_price

    # L5
    black_marble_price = 0.1 # for a dime each
    earnings_black = num_black_marbles * black_marble_price

    # L6
    color_marble_price = 0.2 # for $0.20 each
    earnings_color = num_color_marbles * color_marble_price

    # L7
    total_earnings = earnings_white + earnings_black + earnings_color

    # FA
    answer = total_earnings
    return answer