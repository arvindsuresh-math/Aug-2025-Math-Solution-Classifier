def solve():
    """Index: 6460.
    Returns: the number of white stones Brian has.
    """
    # L1
    grey_stones = 40 # 40 grey stones
    green_stones = 60 # 60 green stones
    total_grey_green_stones = grey_stones + green_stones

    # L2
    grey_percentage_decimal = grey_stones / total_grey_green_stones

    # L3
    total_percentage_decimal = 1.0 # WK
    green_percentage_decimal = total_percentage_decimal - grey_percentage_decimal

    # L5
    total_first_collection_stones = 100 # collection of 100 stones
    white_stones = total_first_collection_stones * green_percentage_decimal

    # FA
    answer = white_stones
    return answer