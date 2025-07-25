def solve():
    """Index: 672.
    Returns: the total amount Harris will spend on carrots in one year.
    """
    # L1
    carrots_per_day = 1 # Harris feeds his dog 1 large organic carrot over the course of 1 day
    days_per_year = 365 # 365 days in a year
    total_carrots = carrots_per_day * days_per_year

    # L2
    carrots_per_bag = 5 # 5 carrots in a 1 pound bag
    total_bags = total_carrots / carrots_per_bag

    # L3
    bag_cost = 2.00 # each bag costs $2.00
    total_cost = bag_cost * total_bags

    # FA
    answer = total_cost
    return answer