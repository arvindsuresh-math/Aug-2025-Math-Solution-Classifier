def solve():
    """Index: 7067.
    Returns: the number of ounces of white paint Marla adds.
    """
    # L1
    blue_paint_ounces = 140 # 140 ounces of blue paint
    blue_paint_percent_decimal = 0.7 # 70% blue paint
    total_paint_ounces = blue_paint_ounces / blue_paint_percent_decimal

    # L2
    blue_paint_percent = 70 # 70% blue paint
    red_paint_percent = 20 # 20% red paint
    total_percentage = 100 # WK
    white_paint_percent_num = total_percentage - blue_paint_percent - red_paint_percent
    percent_factor = 0.01 # WK
    white_paint_ounces = total_paint_ounces * white_paint_percent_num * percent_factor

    # FA
    answer = white_paint_ounces
    return answer