def solve():
    """Index: 2258.
    Returns: the number of stickers Dan has.
    """
    # L1
    tom_multiplier = 3 # 3 times as many stickers as Bob
    bob_stickers = 12 # Bob has 12 stickers
    tom_stickers = tom_multiplier * bob_stickers

    # L2
    dan_multiplier = 2 # two times as many stickers as Tom
    dan_stickers = dan_multiplier * tom_stickers

    # FA
    answer = dan_stickers
    return answer