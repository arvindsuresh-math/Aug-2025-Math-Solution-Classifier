def solve():
    """Index: 3645.
    Returns: the total dollars Geordie spends driving to work and back in a week.
    """
    # L1
    car_toll_cost = 12.50 # The toll is $12.50 per car
    car_drive_days = 3 # drives his car to work three times a week
    car_tolls_cost = car_toll_cost * car_drive_days

    # L2
    motorcycle_toll_cost = 7 # $7 per motorcycle
    motorcycle_drive_days = 2 # his motorcycle to work twice a week
    motorcycle_tolls_cost = motorcycle_toll_cost * motorcycle_drive_days

    # L3
    commute_distance = 14 # commute to work is 14 miles
    work_days_per_week = 5 # five-day workweek
    total_commute_miles_one_way = commute_distance * work_days_per_week

    # L4
    miles_per_gallon = 35 # 35 miles per gallon of gas
    gallons_used_one_way = total_commute_miles_one_way / miles_per_gallon

    # L5
    gas_cost_per_gallon = 3.75 # Gas costs him $3.75 per gallon
    gas_cost_one_way = gas_cost_per_gallon * gallons_used_one_way

    # L6
    total_cost_one_way = car_tolls_cost + motorcycle_tolls_cost + gas_cost_one_way

    # L7
    round_trip_factor = 2 # WK
    total_weekly_cost = total_cost_one_way * round_trip_factor

    # FA
    answer = total_weekly_cost
    return answer