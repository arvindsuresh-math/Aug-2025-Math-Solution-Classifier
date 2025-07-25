def solve():
    """Index: 6512.
    Returns: the total number of cookies Clara sells.
    """
    # L1
    cookies_per_box_type1 = 12 # 12 cookies per box
    boxes_sold_type1 = 50 # sells 50 boxes of the first type
    total_cookies_type1 = cookies_per_box_type1 * boxes_sold_type1

    # L2
    cookies_per_box_type2 = 20 # 20 cookies per box
    boxes_sold_type2 = 80 # 80 boxes of the second type
    total_cookies_type2 = cookies_per_box_type2 * boxes_sold_type2

    # L3
    cookies_per_box_type3 = 16 # 16 cookies per box
    boxes_sold_type3 = 70 # 70 boxes of the third type
    total_cookies_type3 = cookies_per_box_type3 * boxes_sold_type3

    # L4
    total_cookies_sold = total_cookies_type1 + total_cookies_type2 + total_cookies_type3

    # FA
    answer = total_cookies_sold
    return answer