def solve():
    """Index: 1290.
    Returns: the total number of gallons of paint used.
    """
    # L1
    blue_ratio_numerator = 1 # 1 : 2 : 5 ratio
    green_ratio_denominator = 2 # 1 : 2 : 5 ratio
    green_paint_gallons = 6 # 6 gallons of green paint
    blue_paint_gallons = (blue_ratio_numerator / green_ratio_denominator) * green_paint_gallons

    # L2
    white_ratio_numerator = 5 # 1 : 2 : 5 ratio
    white_paint_gallons = (white_ratio_numerator / green_ratio_denominator) * green_paint_gallons

    # L3
    total_paint_gallons = green_paint_gallons + blue_paint_gallons + white_paint_gallons

    # FA
    answer = total_paint_gallons
    return answer