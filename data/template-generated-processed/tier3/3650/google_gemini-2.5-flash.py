def solve():
    """Index: 3650.
    Returns: how much lower the price of the television was than the amount Martin decided to spend.
    """
    # L1
    max_spend = 1000 # no more than $1,000
    initial_discount = 100 # $100 less
    price_after_initial_discount = max_spend - initial_discount

    # L2
    additional_discount_percentage_numerator = 20 # additional 20% off
    percentage_denominator = 100 # WK
    additional_discount_amount = price_after_initial_discount * additional_discount_percentage_numerator / percentage_denominator

    # L3
    final_price = price_after_initial_discount - additional_discount_amount

    # L4
    total_savings = max_spend - final_price

    # FA
    answer = total_savings
    return answer