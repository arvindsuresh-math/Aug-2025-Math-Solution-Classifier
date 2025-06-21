def solve(
    sam_widget_time: int = 10,  # "He can assemble 1 widget every 10 minutes."
    widgets_when_jack_helps: int = 2,  # "they put together 2 complete widgets"
    time_for_two_widgets: int = 15,  # "every 15 minutes" for 2 widgets when Jack helps
    hours_sam: int = 6,  # "Sam worked for 6 hours yesterday"
    hours_jack: int = 4,  # "Jack was able to help out for 4 hours"
    hours_tony: int = 8,  # "Tony worked the entire 8-hour shift"
    total_widgets: int = 68  # "they had completed 68 widgets"
):
    """Index: 399.
    Returns: the time in minutes it takes Tony to assemble one widget.
    """
    #: L1
    # Sam completes a widget every 10 minutes.
    # (Already given as sam_widget_time)
    
    #: L2
    # When Jack helps, they finish 2 widgets in 15 minutes.
    # Therefore, Jack's effective time per widget is 15 minutes.
    jack_widget_time = time_for_two_widgets  # Jack takes 15 minutes per widget per solution logic

    #: L3
    # Sam worked for 6 hours: convert hours to minutes and compute number of widgets.
    sam_total_minutes = hours_sam * 60
    sam_widgets = sam_total_minutes / sam_widget_time  # 6*60/10 = 36

    #: L4
    # Jack worked for 4 hours: convert hours to minutes and compute number of widgets.
    jack_total_minutes = hours_jack * 60
    jack_widgets = jack_total_minutes / jack_widget_time  # 4*60/15 = 16

    #: L5
    # Total widgets assembled by Tony is the remaining widgets.
    tony_widgets = total_widgets - sam_widgets - jack_widgets  # 68 - 36 - 16 = 16

    #: L6
    # Tony worked for 8 hours: convert hours to minutes and compute his assembly time per widget.
    tony_total_minutes = hours_tony * 60
    tony_time_per_widget = tony_total_minutes / tony_widgets  # 8*60/16 = 30

    answer = tony_time_per_widget  # FINAL ANSWER
    return answer