def solve():
    """Index: 6411.
    Returns: the total number of gemstones Rebecca will need.
    """
    # L1
    sets_of_earrings = 4 # 4 sets of earrings
    earrings_per_set = 2 # WK
    total_earrings = earrings_per_set * sets_of_earrings

    # L2
    magnets_per_earring = 2 # she uses two magnets
    total_magnets = magnets_per_earring * total_earrings

    # L3
    half_divisor = 2 # WK
    total_buttons = total_magnets / half_divisor

    # L4
    gemstones_multiplier = 3 # three times as many gemstones
    total_gemstones = total_buttons * gemstones_multiplier

    # FA
    answer = total_gemstones
    return answer