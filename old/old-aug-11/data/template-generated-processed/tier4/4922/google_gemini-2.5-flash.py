def solve():
    """Index: 4922.
    Returns: the amount each person gets after taxes.
    """
    # L1
    over_market_value_decimal = 0.2 # 20% over market value
    base_multiplier = 1 # WK
    sale_multiplier = base_multiplier + over_market_value_decimal

    # L2
    house_value = 500000 # $500,000 house
    selling_price = house_value * sale_multiplier

    # L3
    num_brothers = 3 # his 3 brothers
    james_share = 1 # WK
    total_people_sharing = james_share + num_brothers

    # L4
    amount_before_taxes = selling_price / total_people_sharing

    # L5
    tax_rate_decimal = 0.1 # 10%
    tax_amount = amount_before_taxes * tax_rate_decimal

    # L6
    final_amount_per_person = amount_before_taxes - tax_amount

    # FA
    answer = final_amount_per_person
    return answer