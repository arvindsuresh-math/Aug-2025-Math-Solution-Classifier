from fractions import Fraction

def solve():
    """Index: 1903.
    Returns: the total number of video hours uploaded at the end of the month.
    """
    # L1
    days_in_june = 30 # June has 30 days
    halfway_fraction = Fraction(1, 2) # halfway
    days_halfway_through_june = halfway_fraction * days_in_june

    # L2
    videos_per_day_initial = 10 # uploads 10 one-hour videos
    total_video_hours_halfway = videos_per_day_initial * days_halfway_through_june

    # L3
    doubling_factor = 2 # doubled the number of video hours
    videos_per_day_doubled = videos_per_day_initial * doubling_factor

    # L4
    remaining_days = days_in_june - days_halfway_through_june
    total_video_hours_remaining = remaining_days * videos_per_day_doubled

    # L5
    total_video_hours_month = total_video_hours_remaining + total_video_hours_halfway

    # FA
    answer = total_video_hours_month
    return answer