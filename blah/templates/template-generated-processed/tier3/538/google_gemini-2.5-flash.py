def solve():
    """Index: 538.
    Returns: the selling price of the bag.
    """
    # L1
    bag_cost = 3000 # A luxury bag costs $3000
    profit_percentage_numerator = 15 # 15% profit
    profit_percentage_denominator = 100 # 15% profit
    profit_amount = bag_cost * profit_percentage_numerator / profit_percentage_denominator

    # L2
    selling_price = bag_cost + profit_amount

    # FA
    answer = selling_price
    return answer