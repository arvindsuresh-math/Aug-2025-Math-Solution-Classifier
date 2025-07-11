def solve():
    """Index: 1191.
    Returns: the total amount Wally pays for the bears.
    """
    # L1
    first_bear_price = 4.00 # $4.00 for the first bear
    discount_per_bear = 0.50 # discount of 50 cents per bear
    additional_bear_price = first_bear_price - discount_per_bear

    # L2
    total_bears = 101 # 101 bears
    num_discounted_bears = total_bears - 1

    # L3
    cost_discounted_bears = num_discounted_bears * additional_bear_price

    # L4
    total_cost = cost_discounted_bears + first_bear_price

    # FA
    answer = total_cost
    return answer