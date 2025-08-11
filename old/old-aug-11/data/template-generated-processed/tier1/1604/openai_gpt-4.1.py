def solve():
    """Index: 1604.
    Returns: the number of square feet of paint that can be used to paint the sun.
    """
    # L1
    mary_dragon_paint = 3 # Mary paints a dragon using 3 square feet worth of paint
    mike_more_than_mary = 2 # Mike paints a castle using 2 square feet more paint than Mary used
    mike_castle_paint = mary_dragon_paint + mike_more_than_mary

    # L2
    total_paint = 13 # enough paint in the jar to cover 13 square feet
    sun_paint = total_paint - mary_dragon_paint - mike_castle_paint

    # FA
    answer = sun_paint
    return answer