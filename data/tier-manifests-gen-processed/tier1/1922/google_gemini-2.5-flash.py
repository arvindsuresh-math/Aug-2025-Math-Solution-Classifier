def solve():
    """Index: 1922.
    Returns: how much more money Stormi needs to make to afford the bicycle.
    """
    # L1
    num_cars_washed = 3 # washes 3 cars
    price_per_car = 10 # for $10 each
    money_from_cars = num_cars_washed * price_per_car

    # L2
    num_lawns_mowed = 2 # mows 2 lawns
    price_per_lawn = 13 # for $13 each
    money_from_lawns = num_lawns_mowed * price_per_lawn

    # L3
    total_money_made = money_from_cars + money_from_lawns

    # L4
    bicycle_cost = 80 # bicycle she wants costs $80
    money_needed = bicycle_cost - total_money_made

    # FA
    answer = money_needed
    return answer