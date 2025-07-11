def solve():
    """Index: 1286.
    Returns: the total number of fish Olga has.
    """
    # L1
    yellow_fish_count = 12 # 12 yellow ones
    half_factor = 0.5 # half as many blue ones
    blue_fish_count = yellow_fish_count * half_factor

    # L2
    twice_factor = 2 # twice as many green ones
    green_fish_count = yellow_fish_count * twice_factor

    # L3
    total_fish_count = yellow_fish_count + blue_fish_count + green_fish_count

    # FA
    answer = total_fish_count
    return answer