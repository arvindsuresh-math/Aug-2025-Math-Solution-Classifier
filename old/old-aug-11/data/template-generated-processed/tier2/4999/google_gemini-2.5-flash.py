def solve():
    """Index: 4999.
    Returns: how much money Chastity was left with after spending on candies.
    """
    # L1
    num_lollipops = 4 # 4 lollipops
    lollipop_cost_each = 1.50 # $1.50 each
    lollipops_total_cost = num_lollipops * lollipop_cost_each

    # L2
    num_gummies_packs = 2 # 2 packs of gummies
    gummies_cost_each_pack = 2 # $2 each
    gummies_total_cost = num_gummies_packs * gummies_cost_each_pack

    # L3
    initial_money = 15 # she has $15
    total_candies_cost_displayed = lollipops_total_cost + gummies_total_cost
    money_left = initial_money - total_candies_cost_displayed

    # FA
    answer = money_left
    return answer