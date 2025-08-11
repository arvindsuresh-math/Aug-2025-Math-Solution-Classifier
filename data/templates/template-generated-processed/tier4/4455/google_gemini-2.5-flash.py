def solve():
    """Index: 4455.
    Returns: the initial amount of money Abigail had.
    """
    # L1
    entertainment_cost = 20 # spending $20 on entertainment
    money_left_after_entertainment = 40 # she is left with $40
    money_after_phone_bill = entertainment_cost + money_left_after_entertainment

    # L2
    total_percent = 100 # WK
    phone_bill_percent = 25 # 25% of the remainder on her phone bill
    percent_after_phone_bill = total_percent - phone_bill_percent

    # L3
    value_per_percent_after_food = money_after_phone_bill / percent_after_phone_bill

    # L4
    money_after_food = value_per_percent_after_food * total_percent

    # L5
    food_percent = 60 # 60% of her money on food
    percent_after_food = total_percent - food_percent

    # L6
    value_per_percent_initial = money_after_food / percent_after_food

    # L7
    initial_money = value_per_percent_initial * total_percent

    # FA
    answer = initial_money
    return answer