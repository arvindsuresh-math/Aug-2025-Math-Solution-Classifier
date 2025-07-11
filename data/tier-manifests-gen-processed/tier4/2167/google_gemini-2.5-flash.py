def solve():
    """Index: 2167.
    Returns: the net money the truck driver makes.
    """
    # L1
    driving_hours = 10 # 10 hours
    speed_mph = 30 # 30 miles per hour
    total_miles_driven = driving_hours * speed_mph

    # L2
    miles_per_gallon = 10 # 10 miles per gallon
    gallons_needed = total_miles_driven / miles_per_gallon

    # L3
    cost_per_gallon = 2 # $2 per gallon of gas
    gas_cost = gallons_needed * cost_per_gallon

    # L4
    pay_per_mile = 0.50 # $.50 per mile
    total_earnings = total_miles_driven * pay_per_mile

    # L5
    net_earnings = total_earnings - gas_cost

    # FA
    answer = net_earnings
    return answer