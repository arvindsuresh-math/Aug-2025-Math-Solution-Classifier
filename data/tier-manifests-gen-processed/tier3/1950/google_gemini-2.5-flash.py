def solve():
    """Index: 1950.
    Returns: the cost of each bag of chips.
    """
    # L1
    total_cash_given = 20 # He hands the cashier $20
    change_received = 4 # gets $4 back as change
    total_purchase_cost = total_cash_given - change_received

    # L2
    num_chocolate_bars = 5 # buys 5 chocolate bars
    cost_per_chocolate_bar = 2 # chocolate bars each cost $2
    total_chocolate_cost = num_chocolate_bars * cost_per_chocolate_bar

    # L3
    total_chips_cost = total_purchase_cost - total_chocolate_cost

    # L4
    num_bags_of_chips = 2 # 2 bags of chips
    cost_per_bag_of_chips = total_chips_cost / num_bags_of_chips

    # FA
    answer = cost_per_bag_of_chips
    return answer