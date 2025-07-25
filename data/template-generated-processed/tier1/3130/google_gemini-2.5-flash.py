def solve():
    """Index: 3130.
    Returns: the total miles Jace will travel.
    """
    # L1
    first_drive_hours = 4 # drives for 4 hours straight
    second_drive_hours = 9 # drives for another 9 hours straight
    total_driving_hours = first_drive_hours + second_drive_hours

    # L2
    speed_mph = 60 # 60 miles per hour
    total_miles = speed_mph * total_driving_hours

    # FA
    answer = total_miles
    return answer