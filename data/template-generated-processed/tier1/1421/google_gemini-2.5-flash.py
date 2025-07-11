def solve():
    """Index: 1421.
    Returns: the number of additional plates Xavier should buy.
    """
    # L1
    red_plates = 28 # 28 red plates
    green_plates = 21 # 21 green plates
    total_existing_plates = red_plates + green_plates

    # L2
    plates_needed = 84 # 84 paper plates
    plates_to_buy = plates_needed - total_existing_plates

    # FA
    answer = plates_to_buy
    return answer