def solve():
    """Index: 1753.
    Returns: the total cost for enough sugar substitute to last 90 days.
    """
    # L1
    packets_per_cup = 1 # 1 packet per cup of coffee
    cups_per_day = 2 # 2 coffees a day
    packets_per_day = packets_per_cup * cups_per_day

    # L2
    num_days = 90 # 90 days
    total_packets = num_days * packets_per_day

    # L3
    packets_per_box = 30 # packets come 30 to a box
    num_boxes = total_packets / packets_per_box

    # L4
    cost_per_box = 4 # $4.00 a box
    total_cost = cost_per_box * num_boxes

    # FA
    answer = total_cost
    return answer