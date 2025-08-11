def solve():
    """Index: 7288.
    Returns: the area of the lake in square miles.
    """
    # L1
    time_across_length = 2 # 2 hours to go across the length
    speed = 10 # 10 MPH
    length_of_lake = time_across_length * speed

    # L2
    time_across_width_minutes = 30 # takes 30 minutes
    minutes_per_hour = 60 # WK
    time_across_width_hours = time_across_width_minutes / minutes_per_hour

    # L3
    width_of_lake = speed * time_across_width_hours

    # L4
    lake_area_square_miles = length_of_lake * width_of_lake

    # FA
    answer = lake_area_square_miles
    return answer