def solve():
    """Index: 6173.
    Returns: the number of birthday candles each person will have after sharing equally.
    """
    # L1
    ambika_candles = 4 # Ambika has four birthday candles
    aniyah_multiplier = 6 # 6 times as many birthday candles
    aniyah_candles = ambika_candles * aniyah_multiplier

    # L2
    total_candles = aniyah_candles + ambika_candles

    # L3
    number_of_people = 2 # between themselves
    candles_per_person = total_candles / number_of_people

    # FA
    answer = candles_per_person
    return answer