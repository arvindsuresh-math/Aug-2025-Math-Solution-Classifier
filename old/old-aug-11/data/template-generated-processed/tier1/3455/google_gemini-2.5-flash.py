def solve():
    """Index: 3455.
    Returns: the total number of candles used.
    """
    # L1
    initial_cakes = 8 # bakes 8 cakes
    cakes_given_away = 2 # gives away 2 cakes
    remaining_cakes = initial_cakes - cakes_given_away

    # L2
    candles_per_cake = 6 # puts 6 candles on each cake
    total_candles = remaining_cakes * candles_per_cake

    # FA
    answer = total_candles
    return answer