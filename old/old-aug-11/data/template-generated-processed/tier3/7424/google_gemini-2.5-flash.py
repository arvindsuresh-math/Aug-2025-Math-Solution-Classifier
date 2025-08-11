def solve():
    """Index: 7424.
    Returns: the number of pounds Penny's purchase exceeded the minimum spend.
    """
    # L1
    bulk_price_per_pound = 5 # $5 per pound
    tax_per_pound = 1 # $1 per pound
    cost_per_pound_with_tax = bulk_price_per_pound + tax_per_pound

    # L2
    minimum_spend_dollars = 40 # minimum spend is $40
    minimum_pounds_of_honey = minimum_spend_dollars / bulk_price_per_pound

    # L3
    total_paid = 240 # Penny has paid $240
    pounds_bought_by_penny = total_paid / cost_per_pound_with_tax

    # L4
    exceeded_pounds = pounds_bought_by_penny - minimum_pounds_of_honey

    # FA
    answer = exceeded_pounds
    return answer