def solve():
    """Index: 4992.
    Returns: the difference in miles per gallon between Pria's mileage and the advertised mileage.
    """
    # L1
    total_miles_driven = 372 # drive a total of 372 miles
    gallons_used = 12 # 12-gallon tank
    actual_mileage = total_miles_driven / gallons_used

    # L2
    advertised_mileage = 35 # advertised an estimated gas mileage of 35 miles per gallon
    mileage_difference = advertised_mileage - actual_mileage

    # FA
    answer = mileage_difference
    return answer