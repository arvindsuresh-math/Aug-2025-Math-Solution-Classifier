def solve():
    """Index: 399.
    Returns: the number of minutes it takes Tony to assemble a widget.
    """
    # L3
    sam_hours = 6 # Sam worked for 6 hours
    minutes_per_hour = 60 # WK
    sam_minutes_per_widget = 10 # Sam can assemble 1 widget every 10 minutes
    sam_widgets = sam_hours * minutes_per_hour / sam_minutes_per_widget

    # L4
    jack_hours = 4 # Jack worked for 4 hours
    jack_minutes_per_widget = 15 # Jack finishes a widget in 15 minutes
    jack_widgets = jack_hours * minutes_per_hour / jack_minutes_per_widget

    # L5
    total_widgets = 68 # they had completed 68 widgets
    tony_widgets = total_widgets - sam_widgets - jack_widgets

    # L6
    tony_hours = 8 # Tony worked the entire 8-hour shift
    tony_minutes_per_widget = tony_hours * minutes_per_hour / tony_widgets

    # FA
    answer = tony_minutes_per_widget
    return answer