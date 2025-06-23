def solve(
    sam_time_per_widget: int = 10, # Sam can assemble 1 widget every 10 minutes.
    sam_jack_time_per_2_widgets: int = 15, # When Jack helps, they put together 2 complete widgets every 15 minutes.
    sam_work_hours: int = 6, # Sam worked for 6 hours
    jack_work_hours: int = 4, # Jack was able to help out for 4 hours
    tony_work_hours: int = 8, # Tony worked the entire 8-hour shift.
    total_widgets_completed: int = 68 # At the end of the day, they had completed 68 widgets.
):
    """Index: 399.
    Returns: the time in minutes it takes Tony to assemble a widget.
    """
    #: L1
    sam_time_per_widget = sam_time_per_widget

    #: L2
    jack_time_per_widget = sam_jack_time_per_2_widgets / 2

    #: L3
    sam_widgets_completed = sam_work_hours * 60 / sam_time_per_widget

    #: L4
    jack_widgets_completed = jack_work_hours * 60 / jack_time_per_widget

    #: L5
    tony_widgets_completed = total_widgets_completed - sam_widgets_completed - jack_widgets_completed

    #: L6
    tony_time_per_widget = tony_work_hours * 60 / tony_widgets_completed

    answer = tony_time_per_widget # FINAL ANSWER
    return answer