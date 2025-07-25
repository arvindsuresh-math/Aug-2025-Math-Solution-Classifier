def solve():
    """Index: 5072.
    Returns: the number of butterflies left in the garden.
    """
    # L1
    total_butterflies = 9 # 9 butterflies
    fly_away_denominator = 3 # one-third of them
    butterflies_fly_away = total_butterflies / fly_away_denominator

    # L2
    butterflies_left = total_butterflies - butterflies_fly_away

    # FA
    answer = butterflies_left
    return answer