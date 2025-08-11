def solve():
    """Index: 4771.
    Returns: the total cost of John's car rental and associated expenses.
    """
    # L1
    gas_gallons = 8 # 8 gallons of gas
    gas_price_per_gallon = 3.50 # gas is $3.50 per gallon
    gas_cost = gas_gallons * gas_price_per_gallon

    # L2
    miles_driven = 320 # drove 320 miles
    cost_per_mile = 0.50 # $.50 per mile
    mileage_expense = miles_driven * cost_per_mile

    # L3
    car_rental_cost = 150 # $150 to rent the car
    total_cost = car_rental_cost + gas_cost + mileage_expense

    # FA
    answer = total_cost
    return answer