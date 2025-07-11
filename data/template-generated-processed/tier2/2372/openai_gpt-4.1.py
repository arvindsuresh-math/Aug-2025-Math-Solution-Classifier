def solve():
    """Index: 2372.
    Returns: the total amount Mr. Smith spends on the buffet for his entire family.
    """
    # L1
    adult_buffet_price = 30 # price for the adult buffet is $30
    num_adults = 2 # Mr. Smith and his wife
    adult_total = adult_buffet_price * num_adults

    # L2
    child_buffet_price = 15 # price for the children’s buffet is $15
    num_children = 3 # his 3 children
    children_total = child_buffet_price * num_children

    # L3
    senior_discount_percent = 90 # 90% (100% - 10% discount)
    percent_factor = 0.01 # WK
    senior_buffet_price = adult_buffet_price * senior_discount_percent * percent_factor

    # L5
    num_seniors = 2 # his parents
    seniors_total = senior_buffet_price * num_seniors

    # L6
    family_total = adult_total + children_total + seniors_total

    # FA
    answer = family_total
    return answer