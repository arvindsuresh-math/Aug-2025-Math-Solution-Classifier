def solve():
    """Index: 1893.
    Returns: the profit James makes from the trip.
    """
    # L1
    payment_per_mile = 0.50 # $0.50/mile
    trip_distance = 600 # 600 mile trip
    total_payment = payment_per_mile * trip_distance

    # L2
    truck_mpg = 20 # truck gets 20 miles per gallon
    gallons_needed = trip_distance / truck_mpg

    # L3
    gas_price_per_gallon = 4.00 # $4.00/gallon for gas
    total_gas_cost = gas_price_per_gallon * gallons_needed

    # L4
    profit = total_payment - total_gas_cost

    # FA
    answer = profit
    return answer