def solve():
    """Index: 5817.
    Returns: the total earnings Jenny will make at the better choice of the two neighborhoods.
    """
    # L1
    homes_A = 10 # 10 homes
    boxes_per_home_A = 2 # 2 boxes of cookies
    boxes_sold_A = homes_A * boxes_per_home_A

    # L2
    homes_B = 5 # 5 homes
    boxes_per_home_B = 5 # 5 boxes of cookies
    boxes_sold_B = homes_B * boxes_per_home_B

    # L4
    cost_per_box = 2 # each box of cookies costs $2
    total_earnings = boxes_sold_B * cost_per_box

    # FA
    answer = total_earnings
    return answer