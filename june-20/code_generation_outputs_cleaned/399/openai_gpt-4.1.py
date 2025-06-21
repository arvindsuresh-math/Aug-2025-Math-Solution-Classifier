def solve(
    sam_widget_time: int = 10, # Sam can assemble 1 widget every 10 minutes
    jack_and_sam_widgets: int = 2, # they put together 2 complete widgets every 15 minutes
    jack_and_sam_time: int = 15, # 2 widgets every 15 minutes
    sam_hours: int = 6, # Sam worked for 6 hours
    jack_hours: int = 4, # Jack was able to help out for 4 hours
    tony_hours: int = 8, # Tony worked the entire 8-hour shift
    total_widgets: int = 68 # they had completed 68 widgets
):
    """Index: 399.
    Returns: the number of minutes it takes Tony to assemble one widget.
    """
    #: L3
    sam_widgets = sam_hours * 60 / sam_widget_time

    #: L4
    jack_widget_time = jack_and_sam_time / jack_and_sam_widgets
    jack_widgets = jack_hours * 60 / jack_widget_time

    #: L5
    tony_widgets = total_widgets - sam_widgets - jack_widgets

    #: L6
    tony_widget_time = tony_hours * 60 / tony_widgets

    answer = tony_widget_time # FINAL ANSWER
    return answer