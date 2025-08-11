def solve():
    """Index: 5433.
    Returns: the distance covered by Haley's car in miles.
    """
    # L1
    fuel_ratio_part = 4 # The ratio of fuel used in gallons to the distance covered in miles by Haley's car is 4:7
    distance_ratio_part = 7 # The ratio of fuel used in gallons to the distance covered in miles by Haley's car is 4:7
    total_ratio_parts = fuel_ratio_part + distance_ratio_part

    # L2
    actual_gallons_used = 44 # If Haley's car used 44 gallons of gas
    distance_covered = (distance_ratio_part / total_ratio_parts) * actual_gallons_used * (total_ratio_parts / fuel_ratio_part)

    # FA
    answer = distance_covered
    return answer