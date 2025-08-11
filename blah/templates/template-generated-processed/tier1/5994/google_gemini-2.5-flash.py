def solve():
    """Index: 5994.
    Returns: the number of gemstones Binkie has on his collar.
    """
    # L1
    spaatz_gemstones = 1 # Spaatz has 1 Gemstone on her collar
    less_than_half_amount = 2 # two less than half as many gemstones
    half_frankie_gemstones = spaatz_gemstones + less_than_half_amount

    # L2
    multiplier_for_full = 2 # WK
    frankie_gemstones = half_frankie_gemstones * multiplier_for_full

    # L3
    binkie_multiplier = 4 # four times as many gemstones
    binkie_gemstones = binkie_multiplier * frankie_gemstones

    # FA
    answer = binkie_gemstones
    return answer