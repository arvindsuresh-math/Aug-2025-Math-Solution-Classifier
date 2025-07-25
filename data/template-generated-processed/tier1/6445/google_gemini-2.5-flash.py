def solve():
    """Index: 6445.
    Returns: the total number of pens Tina has.
    """
    # L1
    pink_pens = 12 # 12 pink pens
    fewer_green_than_pink = 9 # 9 fewer green pens than pink pens
    green_pens = pink_pens - fewer_green_than_pink

    # L2
    more_blue_than_green = 3 # 3 more blue pens than green pens
    blue_pens = green_pens + more_blue_than_green

    # L3
    total_pens = pink_pens + green_pens + blue_pens

    # FA
    answer = total_pens
    return answer