def solve():
    """Index: 3002.
    Returns: the total cost to buy enough boxes of wafer cookies.
    """
    # L1
    cookies_per_tray = 80 # 80 wafer cookies
    num_trays = 3 # 3 trays of banana pudding
    total_cookies_needed = cookies_per_tray * num_trays

    # L2
    cookies_per_box = 60 # 60 cookies per box
    num_boxes_needed = total_cookies_needed / cookies_per_box

    # L3
    cost_per_box = 3.50 # Each box costs $3.50
    total_cost = cost_per_box * num_boxes_needed

    # FA
    answer = total_cost
    return answer