def solve():
    """Index: 4895.
    Returns: the number of minutes Christina will drive.
    """
    # L1
    friend_speed_limit = 40 # 40 miles per hour
    friend_driving_hours = 3 # friend drives for 3 hours
    miles_friend_drives = friend_speed_limit * friend_driving_hours

    # L2
    total_drive_miles = 210 # The drive is 210 miles total
    miles_christina_drives = total_drive_miles - miles_friend_drives

    # L3
    christina_speed_limit = 30 # speed limit is 30 miles per hour when Christina is driving
    hours_christina_drives = miles_christina_drives / christina_speed_limit

    # L4
    minutes_per_hour = 60 # WK
    minutes_christina_drives = hours_christina_drives * minutes_per_hour

    # FA
    answer = minutes_christina_drives
    return answer