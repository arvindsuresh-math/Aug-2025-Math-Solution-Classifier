def solve():
    """Index: 3894.
    Returns: the total money Tony spends on gas in 4 weeks.
    """
    # L1
    miles_round_trip = 50 # 50 miles round trip to work
    work_days_per_week = 5 # 5 days a week
    miles_per_week = miles_round_trip * work_days_per_week

    # L2
    number_of_weeks = 4 # in 4 weeks
    total_miles_in_4_weeks = number_of_weeks * miles_per_week

    # L3
    miles_per_gallon = 25 # 25 miles to the gallon
    tank_capacity_gallons = 10 # His tank holds 10 gallons
    miles_per_full_tank = miles_per_gallon * tank_capacity_gallons

    # L4
    number_of_fill_ups = total_miles_in_4_weeks / miles_per_full_tank

    # L5
    total_gallons_needed = number_of_fill_ups * tank_capacity_gallons

    # L6
    cost_per_gallon = 2 # $2 a gallon
    total_cost_of_gas = total_gallons_needed * cost_per_gallon

    # FA
    answer = total_cost_of_gas
    return answer