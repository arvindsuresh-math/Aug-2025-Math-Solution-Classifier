def solve():
    """Index: 1604.
    Returns: the square feet of paint that can be used to paint the sun.
    """
    # L1
    mary_paint_sq_ft = 3 # 3 square feet worth of paint
    mike_more_than_mary = 2 # 2 square feet more paint than Mary used
    castle_paint_sq_ft = mary_paint_sq_ft + mike_more_than_mary

    # L2
    total_initial_paint_sq_ft = 13 # enough paint in the jar to cover 13 square feet
    sun_paint_sq_ft = total_initial_paint_sq_ft - mary_paint_sq_ft - castle_paint_sq_ft

    # FA
    answer = sun_paint_sq_ft
    return answer