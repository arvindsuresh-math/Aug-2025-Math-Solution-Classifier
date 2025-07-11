def solve():
    """Index: 2144.
    Returns: the total amount Sharon will spend on coffee.
    """
    # L1
    vacation_days = 40 # 40 days
    pods_per_day = 3 # 3 cups of coffee (3 coffee pods) every morning
    total_pods_needed = vacation_days * pods_per_day

    # L2
    pods_per_box = 30 # 30 pods to a box
    total_boxes_needed = total_pods_needed / pods_per_box

    # L3
    cost_per_box = 8.00 # $8.00
    total_cost = cost_per_box * total_boxes_needed

    # FA
    answer = total_cost
    return answer