def solve():
    """Index: 6735.
    Returns: the total number of pieces of clothes Avery is donating.
    """
    # L1
    initial_shirts = 4 # 4 shirts
    total_shirts = initial_shirts

    # L2
    pants_multiplier = 2 # twice as many pants as shirts
    total_pants = initial_shirts * pants_multiplier

    # L3
    shorts_divisor = 2 # half as many shorts as pants
    total_shorts = total_pants / shorts_divisor

    # L4
    total_clothes = total_shirts + total_pants + total_shorts

    # FA
    answer = total_clothes
    return answer