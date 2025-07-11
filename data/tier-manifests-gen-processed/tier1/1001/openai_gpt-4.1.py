def solve():
    """Index: 1001.
    Returns: the amount of money left from the plant supplier's earnings.
    """
    # L1
    orchid_price = 50 # $50 each (orchids)
    orchid_qty = 20 # 20 pieces of orchids
    orchid_earnings = orchid_price * orchid_qty

    # L2
    money_plant_price = 25 # $25 (Chinese money plant)
    money_plant_qty = 15 # 15 pieces potted Chinese money plant
    money_plant_earnings = money_plant_price * money_plant_qty

    # L3
    total_earnings = orchid_earnings + money_plant_earnings

    # L4
    worker_pay = 40 # $40 each (worker)
    num_workers = 2 # two workers
    total_worker_pay = worker_pay * num_workers

    # L5
    pots_cost = 150 # new pots worth $150
    total_expenses = total_worker_pay + pots_cost

    # L6
    money_left = total_earnings - total_expenses

    # FA
    answer = money_left
    return answer