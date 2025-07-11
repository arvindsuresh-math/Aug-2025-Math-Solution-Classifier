def solve():
    """Index: 2871.
    Returns: the amount of money Gloria will have left after paying for the cabin.
    """
    # L1
    num_cypress_trees = 20 # 20 cypress trees
    price_per_cypress = 100 # $100 for each cypress tree
    cypress_earnings = num_cypress_trees * price_per_cypress

    # L2
    num_pine_trees = 600 # 600 pine trees
    price_per_pine = 200 # $200 per pine tree
    pine_earnings = num_pine_trees * price_per_pine

    # L3
    num_maple_trees = 24 # 24 maple trees
    price_per_maple = 300 # $300 for a maple tree
    maple_earnings = num_maple_trees * price_per_maple

    # L4
    cash_on_hand = 150 # $150 in cash
    total_funds = cash_on_hand + cypress_earnings + pine_earnings + maple_earnings

    # L5
    cabin_cost = 129000 # $129,000 mountain cabin
    remaining_balance = total_funds - cabin_cost

    # FA
    answer = remaining_balance
    return answer