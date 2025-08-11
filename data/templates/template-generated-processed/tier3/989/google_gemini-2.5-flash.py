def solve():
    """Index: 989.
    Returns: the number of trips it will take to fill the pool.
    """
    # L1
    caleb_gallons = 7 # Caleb can add 7 gallons
    cynthia_gallons = 8 # Cynthia can add 8 gallons
    gallons_per_trip = caleb_gallons + cynthia_gallons

    # L2
    total_gallons_needed = 105 # It will take 105 gallons to fill the pool
    number_of_trips = total_gallons_needed / gallons_per_trip

    # FA
    answer = number_of_trips
    return answer