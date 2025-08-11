def solve():
    """Index: 2372.
    Returns: the total amount Mr. Smith spends on the buffet.
    """
    # L1
    adult_buffet_price = 30 # The price for the adult buffet is $30
    num_adults_no_discount = 2 # Mr. Smith takes his wife
    cost_adults_no_discount = adult_buffet_price * num_adults_no_discount

    # L2
    children_buffet_price = 15 # The price for the children’s buffet is $15
    num_children = 3 # his 3 children
    cost_children = children_buffet_price * num_children

    # L3
    senior_discount_percent_num = 90 # 90% (derived from 10% discount)
    percent_factor = 0.01 # WK
    cost_one_senior = adult_buffet_price * senior_discount_percent_num * percent_factor

    # L5
    num_grandparents = 2 # his parents
    cost_grandparents = cost_one_senior * num_grandparents

    # L6
    total_cost = cost_adults_no_discount + cost_children + cost_grandparents

    # FA
    answer = total_cost
    return answer