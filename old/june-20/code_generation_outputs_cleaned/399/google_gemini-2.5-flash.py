def solve(
        sam_time_per_widget: int = 10, # 1 widget every 10 minutes
        team_widgets_per_time: int = 2, # 2 complete widgets
        team_time_for_widgets: int = 15, # every 15 minutes
        sam_hours_worked: int = 6, # Sam worked for 6 hours
        jack_hours_helped: int = 4, # Jack was able to help out for 4 hours
        tony_hours_worked: int = 8, # Tony worked the entire 8-hour shift
        total_widgets_completed: int = 68 # they had completed 68 widgets
    ):
    """Index: 399.
    Returns: the time it takes Tony to assemble a Widget, in minutes.
    """
    #: L1
    # Sam's rate is 1 widget every 10 minutes, given by sam_time_per_widget.

    #: L2
    # The solution interprets the combined rate of 2 widgets in 15 minutes as Jack's individual rate being 15 minutes per widget.
    jack_time_per_widget = 15

    #: L3
    sam_widgets = sam_hours_worked * 60 / sam_time_per_widget

    #: L4
    jack_widgets = jack_hours_helped * 60 / jack_time_per_widget

    #: L5
    tony_widgets = total_widgets_completed - sam_widgets - jack_widgets

    #: L6
    tony_time_per_widget = tony_hours_worked * 60 / tony_widgets

    answer = tony_time_per_widget # FINAL ANSWER
    return answer