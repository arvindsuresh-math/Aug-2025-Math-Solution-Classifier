def solve():
    """Index: 1191.
    Returns: the total amount Wally pays for 101 bears.
    """
    # L1
    first_bear_price = 4.00 # $4.00 for the first bear
    discount_per_bear = 0.50 # a discount of 50 cents per bear is given after that
    additional_bear_price = first_bear_price - discount_per_bear

    # L2
    total_bears = 101 # Wally bought 101 bears
    additional_bears = total_bears - 1

    # L3
    total_additional_cost = additional_bears * additional_bear_price

    # L4
    total_cost = total_additional_cost + first_bear_price

    # FA
    answer = total_cost
    return answer