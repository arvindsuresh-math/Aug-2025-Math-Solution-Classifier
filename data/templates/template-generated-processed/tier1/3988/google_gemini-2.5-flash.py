def solve():
    """Index: 3988.
    Returns: the total value of all the treats DJ Snake received.
    """
    # L1
    num_nights = 2 # two nights
    cost_per_night = 4000 # $4000 per night
    moksi_hotel_cost = num_nights * cost_per_night

    # L2
    lil_jon_car_value = 30000 # car worth $30000
    total_moksi_lil_jon = moksi_hotel_cost + lil_jon_car_value

    # L3
    wynter_multiplier = 4 # four times the value of the car
    wynter_house_value = wynter_multiplier * lil_jon_car_value

    # L4
    total_treats_value = wynter_house_value + total_moksi_lil_jon

    # FA
    answer = total_treats_value
    return answer