def solve():
    """Index: 2129.
    Returns: the number of ducks the farmer sold.
    """
    # L1
    additional_earnings_from_wheelbarrow = 60 # earns another $60
    wheelbarrow_sale_multiplier = 2 # double what the farmer paid
    wheelbarrow_cost = additional_earnings_from_wheelbarrow / wheelbarrow_sale_multiplier

    # L2
    earnings_spent_fraction_denominator = 2 # half his earnings
    total_fowl_earnings = wheelbarrow_cost / (1 / earnings_spent_fraction_denominator)

    # L3
    num_chickens_sold = 5 # sells 5 chickens
    chicken_price = 8 # chickens for $8
    chicken_earnings = num_chickens_sold * chicken_price

    # L4
    duck_earnings = total_fowl_earnings - chicken_earnings

    # L5
    duck_price = 10 # ducks for $10
    num_ducks_sold = duck_earnings / duck_price

    # FA
    answer = num_ducks_sold
    return answer