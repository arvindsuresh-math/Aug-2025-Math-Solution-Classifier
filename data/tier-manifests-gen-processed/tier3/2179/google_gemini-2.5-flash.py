def solve():
    """Index: 2179.
    Returns: the number of additional hours the next podcast needs to be.
    """
    # L1
    first_podcast_minutes = 45 # The first podcast was 45 minutes long
    twice_factor = 2 # twice as long as that
    second_podcast_minutes = twice_factor * first_podcast_minutes

    # L2
    third_podcast_hours = 1 # 1 hour and 45 minutes long
    third_podcast_minutes_extra = 45 # 1 hour and 45 minutes long
    minutes_per_hour = 60 # 1 hour is 60 mins
    third_podcast_total_minutes = third_podcast_hours * minutes_per_hour + third_podcast_minutes_extra

    # L3
    fourth_podcast_minutes = 60 # His fourth podcast is 1 hour long
    total_downloaded_minutes = first_podcast_minutes + second_podcast_minutes + third_podcast_total_minutes + fourth_podcast_minutes

    # L4
    total_downloaded_hours = total_downloaded_minutes / minutes_per_hour

    # L5
    total_drive_hours = 6 # a 6-hour drive planned out
    additional_hours_needed = total_drive_hours - total_downloaded_hours

    # FA
    answer = additional_hours_needed
    return answer