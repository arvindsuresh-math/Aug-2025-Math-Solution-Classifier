def solve():
    """Index: 4386.
    Returns: the total amount of money Jolene raised so far.
    """
    # L1
    num_families_babysat = 4 # 4 families
    babysitting_rate_per_family = 30 # $30 each
    babysitting_money = num_families_babysat * babysitting_rate_per_family

    # L2
    num_cars_washed = 5 # 5 neighbors
    car_wash_rate_per_car = 12 # $12 each
    car_wash_money = num_cars_washed * car_wash_rate_per_car

    # L3
    total_raised = babysitting_money + car_wash_money

    # FA
    answer = total_raised
    return answer