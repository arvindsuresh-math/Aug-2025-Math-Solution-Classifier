def solve():
    """Index: 4890.
    Returns: the final number of miles on Marcus' car.
    """
    # L1
    tank_volume = 20 # holds 20 gallons of gas
    num_fill_ups = 2 # filled his empty gas tank twice
    total_gallons = tank_volume * num_fill_ups

    # L2
    fuel_mileage = 30 # gets 30 miles per gallon
    miles_driven = total_gallons * fuel_mileage

    # L3
    initial_miles = 1728 # car had 1728 miles on it
    final_miles = initial_miles + miles_driven

    # FA
    answer = final_miles
    return answer