def solve():
    """Index: 1421.
    Returns: the number of additional plates Xavier should buy.
    """
    # L1
    red_plates = 28 # 28 red plates
    green_plates = 21 # 21 green plates
    total_colored_plates = red_plates + green_plates

    # L2
    required_plates = 84 # needs 84 paper plates
    plates_to_buy = required_plates - total_colored_plates

    # FA
    answer = plates_to_buy
    return answer