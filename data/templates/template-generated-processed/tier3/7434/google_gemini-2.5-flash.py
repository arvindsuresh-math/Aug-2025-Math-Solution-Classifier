def solve():
    """Index: 7434.
    Returns: the total amount Travis can take home.
    """
    # L1
    total_apples = 10000 # Travis has 10000 apples
    apples_per_box = 50 # Fifty apples can fit in each box
    total_boxes = total_apples / apples_per_box

    # L2
    price_per_box = 35 # sells each box of apples for $35
    total_amount_home = total_boxes * price_per_box

    # FA
    answer = total_amount_home
    return answer