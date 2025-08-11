def solve():
    """Index: 6747.
    Returns: the amount each person pays toward gas monthly.
    """
    # L1
    days_per_week = 5 # 5 days a week
    weeks_per_month = 4 # 4 weeks a month
    monthly_commutes_days = days_per_week * weeks_per_month

    # L2
    commute_one_way_miles = 21 # 21 miles one way
    two_ways_factor = 2 # WK
    commute_round_trip_miles = commute_one_way_miles * two_ways_factor

    # L3
    total_monthly_miles = commute_round_trip_miles * monthly_commutes_days

    # L4
    car_mpg = 30 # Carson's car gets 30 miles/gallon
    gallons_needed_monthly = total_monthly_miles / car_mpg

    # L5
    gas_cost_per_gallon = 2.50 # gas costs $2.50/gallon
    total_monthly_gas_cost = gallons_needed_monthly * gas_cost_per_gallon

    # L6
    num_friends = 5 # five of his friends
    cost_per_person_monthly = total_monthly_gas_cost / num_friends

    # FA
    answer = cost_per_person_monthly
    return answer