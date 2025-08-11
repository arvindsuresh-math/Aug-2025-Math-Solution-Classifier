def solve():
    """Index: 6180.
    Returns: the total ounces of paint used.
    """
    # L1
    paint_per_large_canvas = 3 # 3 ounces of paint for every large canvas
    num_large_paintings = 3 # completed 3 large paintings
    paint_used_large = paint_per_large_canvas * num_large_paintings

    # L2
    paint_per_small_canvas = 2 # 2 ounces of paint for every small canvas
    num_small_paintings = 4 # 4 small paintings
    paint_used_small = paint_per_small_canvas * num_small_paintings

    # L3
    total_paint_used = paint_used_large + paint_used_small

    # FA
    answer = total_paint_used
    return answer