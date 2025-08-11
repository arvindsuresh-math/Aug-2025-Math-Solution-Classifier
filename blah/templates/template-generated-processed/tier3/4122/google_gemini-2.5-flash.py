def solve():
    """Index: 4122.
    Returns: the total number of hours it will take to process all pictures.
    """
    # L1
    minutes_per_picture = 2 # 2 minutes to process each picture
    total_pictures = 960 # 960 pictures
    total_minutes = minutes_per_picture * total_pictures

    # L2
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer