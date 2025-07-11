def solve():
    """Index: 1001.
    Returns: the amount of money left from the plant supplier's earnings.
    """
    # L1
    orchid_price_per_piece = 50 # $50 each
    num_orchids_sold = 20 # 20 pieces of orchids
    earnings_orchids = orchid_price_per_piece * num_orchids_sold

    # L2
    money_plant_price_per_piece = 25 # $25
    num_money_plants_sold = 15 # 15 pieces potted Chinese money plant
    earnings_money_plants = money_plant_price_per_piece * num_money_plants_sold

    # L3
    total_earnings = earnings_orchids + earnings_money_plants

    # L4
    worker_pay_per_person = 40 # $40 each
    num_workers = 2 # two workers
    total_worker_pay = worker_pay_per_person * num_workers

    # L5
    cost_new_pots = 150 # new pots worth $150
    total_expenses = total_worker_pay + cost_new_pots

    # L6
    money_left = total_earnings - total_expenses

    # FA
    answer = money_left
    return answer