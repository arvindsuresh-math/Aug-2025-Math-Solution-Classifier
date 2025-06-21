def solve(
    kitchen_length: int = 12,  # "12 foot" from the kitchen dimensions
    kitchen_width: int = 16,   # "16 foot" from the kitchen dimensions
    ceiling_height: int = 10,  # "10 foot high ceilings"
    paint_rate: int = 40       # "40 square feet per hour"
):
    """Index: 3518.
    Returns: the total number of hours required to paint the kitchen.
    """
    #: L1
    area_one_short_wall = kitchen_length * ceiling_height  # 12 * 10 = 120 sq ft

    #: L2
    total_area_short_walls = area_one_short_wall * 2  # 120 * 2 = 240 sq ft

    #: L3
    area_one_long_wall = kitchen_width * ceiling_height  # 16 * 10 = 160 sq ft

    #: L4
    total_area_long_walls = area_one_long_wall * 2  # 160 * 2 = 320 sq ft

    #: L5
    total_wall_area = total_area_short_walls + total_area_long_walls  # 240 + 320 = 560 sq ft

    #: L6
    total_area_with_coats = total_wall_area * 3  # 560 * 3 = 1680 sq ft (1 coat of primer + 2 coats of paint)

    #: L7
    total_hours = total_area_with_coats / paint_rate  # 1680 / 40 = 42 hours

    answer = total_hours  # FINAL ANSWER
    return answer