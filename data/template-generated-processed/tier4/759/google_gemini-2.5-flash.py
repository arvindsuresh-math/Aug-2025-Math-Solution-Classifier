def solve():
    """Index: 759.
    Returns: the total money Tom made (profit).
    """
    # L1
    flour_needed_pounds = 500 # 500 pounds of flour
    flour_bag_size_pounds = 50 # 50-pound bags of flour
    num_flour_bags = flour_needed_pounds / flour_bag_size_pounds

    # L2
    cost_per_flour_bag = 20 # $20
    total_flour_cost = cost_per_flour_bag * num_flour_bags

    # L3
    salt_needed_pounds = 10 # 10 pounds of salt
    cost_per_pound_salt = 0.2 # $.2 a pound
    total_salt_cost = salt_needed_pounds * cost_per_pound_salt

    # L4
    promotion_cost = 1000 # $1000 promoting everything
    total_expenses = promotion_cost + total_flour_cost + total_salt_cost

    # L5
    ticket_price = 20 # $20 each
    num_tickets_sold = 500 # sells 500 tickets
    total_ticket_revenue = ticket_price * num_tickets_sold

    # L6
    profit = total_ticket_revenue - total_expenses

    # FA
    answer = profit
    return answer