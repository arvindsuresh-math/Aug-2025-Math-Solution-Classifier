def solve(
    sam_widget_time: int = 10,  # Sam can assemble 1 widget every 10 minutes
    sam_work_hours: int = 6,  # Sam worked for 6 hours
    jack_work_hours: int = 4,  # Jack was able to help out for 4 hours
    jack_widget_time: int = 15,  # Jack and Sam complete 2 widgets in 15 minutes
    tony_work_hours: int = 8,  # Tony worked the entire 8-hour shift
    total_widgets_completed: int = 68  # At the end of the day, they had completed 68 widgets
):
    """Index: 399.
    Returns: the time it takes Tony to assemble a widget, in minutes.
    """
    #: L3
    sam_widgets = sam_work_hours * 60 / sam_widget_time

    #: L4
    jack_widgets = jack_work_hours * 60 / jack_widget_time

    #: L5
    tony_widgets = total_widgets_completed - sam_widgets - jack_widgets

    #: L6
    tony_widget_time = tony_work_hours * 60 / tony_widgets

    answer = tony_widget_time  # FINAL ANSWER
    return answer