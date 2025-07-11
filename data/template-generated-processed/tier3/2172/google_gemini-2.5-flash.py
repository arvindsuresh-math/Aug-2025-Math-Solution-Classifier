def solve():
    """Index: 2172.
    Returns: the total number of candles in the house.
    """
    # L1
    bedroom_candles = 20 # twenty candles in her bedroom
    twice_factor = 2 # twice the number
    living_room_candles = bedroom_candles / twice_factor

    # L2
    donovan_candles = 20 # brings in 20 more candles
    total_candles = living_room_candles + bedroom_candles + donovan_candles

    # FA
    answer = total_candles
    return answer