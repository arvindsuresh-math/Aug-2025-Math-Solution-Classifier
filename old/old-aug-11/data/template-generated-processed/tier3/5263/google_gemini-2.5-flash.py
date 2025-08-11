def solve():
    """Index: 5263.
    Returns: the amount Sue has to pay for the car.
    """
    # L1
    days_in_a_week = 7 # WK
    sister_days_per_week = 4 # Sue's sister will drive the car 4 days a week
    sue_days_per_week = days_in_a_week - sister_days_per_week

    # L2
    car_cost = 2100 # buy a $2,100 car
    sue_payment = car_cost * sue_days_per_week / days_in_a_week

    # FA
    answer = sue_payment
    return answer