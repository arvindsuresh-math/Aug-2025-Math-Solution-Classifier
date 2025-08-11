def solve():
    """Index: 6972.
    Returns: the total calories inside the box.
    """
    # L1
    cookies_per_bag = 20 # 20 cookies inside
    bags_per_box = 4 # 4 bags in total
    total_cookies_in_box = cookies_per_bag * bags_per_box

    # L2
    calories_per_cookie = 20 # each cookie is 20 calories
    total_calories_in_box = calories_per_cookie * total_cookies_in_box

    # FA
    answer = total_calories_in_box
    return answer