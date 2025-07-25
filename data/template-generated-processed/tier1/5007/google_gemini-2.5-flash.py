def solve():
    """Index: 5007.
    Returns: the difference in the number of cookies between boxes and bags.
    """
    # L1
    num_boxes = 8 # 8 boxes
    cookies_per_box = 12 # Each box has 12 cookies
    total_cookies_boxes = num_boxes * cookies_per_box

    # L2
    num_bags = 9 # 9 bags
    cookies_per_bag = 7 # Each bag has 7 cookies
    total_cookies_bags = num_bags * cookies_per_bag

    # L3
    difference_cookies = total_cookies_boxes - total_cookies_bags

    # FA
    answer = difference_cookies
    return answer