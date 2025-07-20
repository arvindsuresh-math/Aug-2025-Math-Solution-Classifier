def solve():
    """Index: 4349.
    Returns: the number of minutes after 6:00 AM Uranus first appears.
    """
    # L2
    mars_visible_until_hour = 12 # Mars can be seen until 12:10 AM
    mars_visible_until_minute = 10 # Mars can be seen until 12:10 AM
    jupiter_delay_hours = 2 # 2 hours and 41 minutes later
    jupiter_intermediate_hour = mars_visible_until_hour + jupiter_delay_hours
    jupiter_intermediate_minute = mars_visible_until_minute

    # L3
    jupiter_delay_minutes = 41 # 2 hours and 41 minutes later
    jupiter_appearance_minute = jupiter_intermediate_minute + jupiter_delay_minutes
    jupiter_appearance_hour = jupiter_intermediate_hour

    # L5
    uranus_delay_hours = 3 # 3 hours and 16 minutes after Jupiter makes its first appearance
    uranus_intermediate_hour = jupiter_appearance_hour + uranus_delay_hours
    uranus_intermediate_minute = jupiter_appearance_minute

    # L6
    uranus_delay_minutes = 16 # 3 hours and 16 minutes after Jupiter makes its first appearance
    minutes_per_hour = 60 # WK
    uranus_total_minutes_from_intermediate = uranus_intermediate_minute + uranus_delay_minutes
    uranus_appearance_hour = uranus_intermediate_hour + (uranus_total_minutes_from_intermediate // minutes_per_hour)
    uranus_appearance_minute = uranus_total_minutes_from_intermediate % minutes_per_hour
    uranus_intermediate_minute_plus_delay = uranus_total_minutes_from_intermediate

    # L7
    reference_hour = 6 # 6:00 AM
    reference_minute = 0 # 6:00 AM
    minutes_after_6am = uranus_appearance_minute - reference_minute

    # FA
    answer = minutes_after_6am
    return answer