def solve():
    """Index: 3638.
    Returns: how much more money Einstein needs to raise to reach his goal.
    """
    # L1
    num_pizza_boxes = 15 # 15 boxes of pizzas
    price_per_pizza_box = 12 # $12
    pizza_revenue = num_pizza_boxes * price_per_pizza_box

    # L2
    num_fries_packs = 40 # 40 packs of potato fries
    price_per_fries_pack = 0.30 # $0.30
    fries_revenue = num_fries_packs * price_per_fries_pack

    # L3
    num_soda_cans = 25 # 25 cans of soda
    price_per_soda_can = 2 # $2
    soda_revenue = num_soda_cans * price_per_soda_can

    # L4
    total_collected_amount = pizza_revenue + fries_revenue + soda_revenue

    # L5
    fundraising_goal = 500 # raise $500
    money_needed = fundraising_goal - total_collected_amount

    # FA
    answer = money_needed
    return answer