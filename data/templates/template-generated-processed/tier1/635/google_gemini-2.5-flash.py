def solve():
    """Index: 635.
    Returns: the number of cheesecakes left to be sold.
    """
    # L1
    cheesecakes_display = 10 # 10 cheesecakes on the display
    cheesecakes_fridge = 15 # 15 more are still in the fridge
    total_cheesecakes = cheesecakes_display + cheesecakes_fridge

    # L2
    sold_cheesecakes = 7 # sold 7 cheesecakes from the display
    cheesecakes_left_to_sell = total_cheesecakes - sold_cheesecakes

    # FA
    answer = cheesecakes_left_to_sell
    return answer