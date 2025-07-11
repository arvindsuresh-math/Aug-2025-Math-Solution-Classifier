def solve():
    """Index: 1922.
    Returns: the additional amount Stormi needs to afford the bicycle.
    """
    # L1
    cars_washed = 3 # washes 3 cars
    money_per_car = 10 # $10 each
    money_from_cars = cars_washed * money_per_car

    # L2
    lawns_mowed = 2 # mows 2 lawns
    money_per_lawn = 13 # $13 each
    money_from_lawns = lawns_mowed * money_per_lawn

    # L3
    total_money = money_from_cars + money_from_lawns

    # L4
    bike_cost = 80 # bicycle she wants costs $80
    money_needed = bike_cost - total_money

    # FA
    answer = money_needed
    return answer