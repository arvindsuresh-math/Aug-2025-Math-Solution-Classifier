def solve():
    """Index: 4399.
    Returns: the amount of dollars Lily has left for coffee.
    """
    # L1
    celery_cost = 5 # celery for $5
    bread_cost = 8 # bread for $8
    celery_bread_cost = celery_cost + bread_cost

    # L2
    cereal_original_price = 12 # $12
    cereal_discount_percent_num = 50 # 50% off $12
    percent_divisor = 100 # WK
    cereal_cost = cereal_original_price * (cereal_discount_percent_num / percent_divisor)

    # L3
    milk_total_percent = 100 # WK
    milk_discount_percent = 10 # 10% off $10
    milk_paid_percent_num = milk_total_percent - milk_discount_percent

    # L4
    milk_original_price = 10 # $10
    percent_factor = 0.01 # WK
    milk_cost = milk_original_price * milk_paid_percent_num * percent_factor

    # L5
    potato_unit_price = 1 # $1 each
    num_potatoes = 6 # buys 6
    potatoes_cost = potato_unit_price * num_potatoes

    # L6
    initial_money = 60 # She has $60
    money_left_for_coffee = initial_money - celery_bread_cost - cereal_cost - milk_cost - potatoes_cost

    # FA
    answer = money_left_for_coffee
    return answer