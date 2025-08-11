def solve():
    """Index: 4116.
    Returns: the total bill for the ice cream.
    """
    # L1
    pierre_scoops = 3 # 3 scoops
    cost_per_scoop = 2 # Each scoop is $2
    pierre_cost = pierre_scoops * cost_per_scoop

    # L2
    mom_scoops = 4 # his mom gets 4
    mom_cost = mom_scoops * cost_per_scoop

    # L3
    total_bill = pierre_cost + mom_cost

    # FA
    answer = total_bill
    return answer