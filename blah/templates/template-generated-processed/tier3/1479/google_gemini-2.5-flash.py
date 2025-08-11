def solve():
    """Index: 1479.
    Returns: the number of days before Wallace can fulfill the customer's order.
    """
    # L1
    customer_order_bags = 60 # customer order for 60 bags of jerky
    bags_already_made = 20 # he has 20 bags of jerky already made
    bags_needed_more = customer_order_bags - bags_already_made

    # L2
    bags_per_batch = 10 # Each batch can make 10 bags of jerky
    days_to_fulfill_order = bags_needed_more / bags_per_batch

    # FA
    answer = days_to_fulfill_order
    return answer