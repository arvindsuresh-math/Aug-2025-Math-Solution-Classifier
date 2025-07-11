def solve():
    """Index: 2167.
    Returns: the net money the truck driver makes after paying for gas.
    """
    # L1
    hours_driven = 10 # drives for 10 hours
    speed_mph = 30 # drives at a rate of 30 miles per hour
    total_miles = hours_driven * speed_mph

    # L2
    miles_per_gallon = 10 # can drive 10 miles per gallon
    gallons_needed = total_miles / miles_per_gallon

    # L3
    cost_per_gallon = 2 # $2 per gallon of gas
    total_gas_cost = gallons_needed * cost_per_gallon

    # L4
    pay_per_mile = 0.50 # paid $0.50 per mile
    total_pay = total_miles * pay_per_mile

    # L5
    net_earnings = total_pay - total_gas_cost

    # FA
    answer = net_earnings
    return answer