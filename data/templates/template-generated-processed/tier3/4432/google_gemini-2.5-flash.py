def solve():
    """Index: 4432.
    Returns: the number of photos Shane took each week in February.
    """
    # L1
    photos_per_day_january = 2 # 2 photos every day
    days_in_january = 31 # WK
    photos_in_january = photos_per_day_january * days_in_january

    # L2
    total_photos_first_two_months = 146 # 146 photos in the first 2 months
    photos_in_february = total_photos_first_two_months - photos_in_january

    # L3
    weeks_in_february = 4 # WK
    photos_per_week_february = photos_in_february / weeks_in_february

    # FA
    answer = photos_per_week_february
    return answer