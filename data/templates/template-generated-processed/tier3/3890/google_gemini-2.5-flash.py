def solve():
    """Index: 3890.
    Returns: the distance of the fourth buoy from the beach.
    """
    # L1
    distance_to_third_buoy = 72 # third buoy, they have swum out 72 meters
    third_buoy_number = 3 # third buoy
    distance_per_buoy_interval = distance_to_third_buoy / third_buoy_number

    # L2
    fourth_buoy_number = 4 # fourth buoy
    distance_to_fourth_buoy = distance_per_buoy_interval * fourth_buoy_number

    # FA
    answer = distance_to_fourth_buoy
    return answer