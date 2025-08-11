def solve():
    """Index: 2258.
    Returns: the number of stickers Dan has.
    """
    # L1
    bob_stickers = 12 # Bob has 12 stickers
    tom_times_bob = 3 # Tom has 3 times as many stickers as Bob
    tom_stickers = tom_times_bob * bob_stickers

    # L2
    dan_times_tom = 2 # Dan has two times as many stickers as Tom
    dan_stickers = dan_times_tom * tom_stickers

    # FA
    answer = dan_stickers
    return answer