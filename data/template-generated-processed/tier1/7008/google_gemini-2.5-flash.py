def solve():
    """Index: 7008.
    Returns: the total square feet the art collection takes up.
    """
    # L1
    square_painting_side = 6 # three square 6-foot by 6-foot paintings
    area_square_painting_each = square_painting_side * square_painting_side

    # L2
    small_painting_length = 2 # four small 2-foot by 3-foot paintings
    small_painting_width = 3 # four small 2-foot by 3-foot paintings
    area_small_painting_each = small_painting_length * small_painting_width

    # L3
    large_painting_length = 10 # one large 10-foot by 15-foot painting
    large_painting_width = 15 # one large 10-foot by 15-foot painting
    area_large_painting_each = large_painting_length * large_painting_width

    # L4
    num_square_paintings = 3 # three square 6-foot by 6-foot paintings
    total_area_square_paintings = num_square_paintings * area_square_painting_each

    # L5
    num_small_paintings = 4 # four small 2-foot by 3-foot paintings
    total_area_small_paintings = num_small_paintings * area_small_painting_each

    # L6
    total_collection_area = area_large_painting_each + total_area_square_paintings + total_area_small_paintings

    # FA
    answer = total_collection_area
    return answer