def solve():
    """Index: 2144.
    Returns: the total amount Sharon will spend on coffee for her vacation.
    """
    # L1
    num_days = 40 # She'll be on vacation for 40 days
    pods_per_day = 3 # drinks 3 cups of coffee/pods per day
    total_pods_needed = num_days * pods_per_day

    # L2
    pods_per_box = 30 # coffee pods come 30 in a box
    num_boxes_needed = total_pods_needed / pods_per_box

    # L3
    price_per_box = 8.00 # Each box costs $8.00
    total_cost = price_per_box * num_boxes_needed

    # FA
    answer = total_cost
    return answer