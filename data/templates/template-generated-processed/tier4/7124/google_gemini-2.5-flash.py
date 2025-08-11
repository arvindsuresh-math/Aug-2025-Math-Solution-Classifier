def solve():
    """Index: 7124.
    Returns: the total cost of buying ten oranges and ten mangoes at the new prices.
    """
    # L1
    orange_initial_price = 40 # $40
    price_increase_percent_numerator = 15 # increased the prices of goods at his store by 15%
    percent_denominator = 100 # WK
    orange_price_increase = (price_increase_percent_numerator / percent_denominator) * orange_initial_price

    # L2
    orange_new_price = orange_price_increase + orange_initial_price

    # L3
    mango_initial_price = 50 # the price of purchasing a mango was $50
    mango_price_increase = (price_increase_percent_numerator / percent_denominator) * mango_initial_price

    # L4
    mango_new_price = mango_initial_price + mango_price_increase

    # L5
    num_oranges = 10 # ten oranges
    total_cost_oranges = orange_new_price * num_oranges

    # L6
    num_mangoes = 10 # ten mangoes
    total_cost_mangoes = mango_new_price * num_mangoes

    # L7
    total_cost_all = total_cost_mangoes + total_cost_oranges

    # FA
    answer = total_cost_all
    return answer