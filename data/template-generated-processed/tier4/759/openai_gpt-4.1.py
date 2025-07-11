def solve():
    """Index: 759.
    Returns: the profit Tom made from selling tickets after expenses.
    """
    # L1
    flour_needed_pounds = 500 # He needs 500 pounds of flour
    flour_bag_pounds = 50 # 50-pound bags of flour
    flour_bags_needed = flour_needed_pounds / flour_bag_pounds

    # L2
    flour_bag_cost = 20 # $20 per 50-pound bag
    total_flour_cost = flour_bag_cost * flour_bags_needed

    # L3
    salt_needed_pounds = 10 # He needs 10 pounds of salt
    salt_cost_per_pound = 0.2 # salt cost $.2 a pound
    total_salt_cost = salt_needed_pounds * salt_cost_per_pound

    # L4
    promotion_cost = 1000 # He also spends $1000 promoting everything
    total_expenses = promotion_cost + total_flour_cost + total_salt_cost

    # L5
    ticket_price = 20 # sells tickets for $20 each
    tickets_sold = 500 # sells 500 tickets
    total_ticket_revenue = ticket_price * tickets_sold

    # L6
    profit = total_ticket_revenue - total_expenses

    # FA
    answer = profit
    return answer