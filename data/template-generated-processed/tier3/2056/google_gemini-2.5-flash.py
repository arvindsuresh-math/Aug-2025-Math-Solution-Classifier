def solve():
    """Index: 2056.
    Returns: the number of packs of wipes Randy needs.
    """
    # L1
    wipes_per_day = 2 # Randy walks his dog twice a day. After each walk, he wipes his dog's paws off with a baby wipe.
    wipes_per_pack = 120 # 120 wipes per pack
    days_per_pack = wipes_per_pack / wipes_per_day

    # L2
    total_days_needed = 360 # for 360 days
    packs_needed = total_days_needed / days_per_pack

    # FA
    answer = packs_needed
    return answer