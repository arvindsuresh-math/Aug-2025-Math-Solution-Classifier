def solve():
    """Index: 5215.
    Returns: the number of hairs Anya has to grow back.
    """
    # L1
    hairs_washed_down_drain = 32 # washes 32 hairs down the drain
    brush_divisor = 2 # half that amount
    hairs_brushed_out = hairs_washed_down_drain / brush_divisor

    # L2
    extra_hair_needed = 1 # one more hair
    hairs_to_grow_back = hairs_brushed_out + hairs_washed_down_drain + extra_hair_needed

    # FA
    answer = hairs_to_grow_back
    return answer