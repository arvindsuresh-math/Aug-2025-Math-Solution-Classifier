def solve():
    """Index: 399.
    Returns: the time it takes Tony to assemble a Widget in minutes.
    """
    # L1
    sam_time_per_widget = 10 # He can assemble 1 widget every 10 minutes.

    # L2
    jack_time_per_widget = 15 # So it takes Jack 15 minutes to complete a widget.

    # L3
    sam_hours_worked = 6 # Sam worked for 6 hours
    minutes_per_hour = 60 # WK
    sam_widgets_completed = sam_hours_worked * minutes_per_hour / sam_time_per_widget

    # L4
    jack_hours_worked = 4 # Jack was able to help out for 4 hours
    jack_widgets_completed = jack_hours_worked * minutes_per_hour / jack_time_per_widget

    # L5
    total_widgets_completed = 68 # At the end of the day, they had completed 68 widgets.
    tony_widgets_completed = total_widgets_completed - sam_widgets_completed - jack_widgets_completed

    # L6
    tony_hours_worked = 8 # Tony worked the entire 8-hour shift.
    tony_time_per_widget = tony_hours_worked * minutes_per_hour / tony_widgets_completed

    # FA
    answer = tony_time_per_widget
    return answer