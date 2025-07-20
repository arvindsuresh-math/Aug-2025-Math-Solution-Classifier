def solve():
    """Index: 6910.
    Returns: the total number of widgets John makes in a week.
    """
    # L1
    hours_per_day = 8 # works for 8 hours a day
    days_per_week = 5 # 5 days a week
    total_hours_per_week = hours_per_day * days_per_week

    # L2
    widgets_per_hour = 20 # 20 widgets an hour
    total_widgets_per_week = widgets_per_hour * total_hours_per_week

    # FA
    answer = total_widgets_per_week
    return answer