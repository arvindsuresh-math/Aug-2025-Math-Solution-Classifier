def solve():
    """Index: 4709.
    Returns: the total square feet Elisa paints.
    """
    # L1
    monday_paint = 30 # 30 square feet of her house's walls

    # L2
    twice_amount = 2 # twice that amount
    tuesday_paint = twice_amount * monday_paint

    # L3
    half_amount_divisor = 2 # half as many square feet
    wednesday_paint = monday_paint / half_amount_divisor

    # L4
    total_paint = monday_paint + tuesday_paint + wednesday_paint

    # FA
    answer = total_paint
    return answer