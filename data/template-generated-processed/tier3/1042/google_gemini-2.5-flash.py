def solve():
    """Index: 1042.
    Returns: the number of candy bars Kim had saved.
    """
    # L1
    candy_bars_per_week = 2 # 2 candy bars a week
    total_weeks = 16 # After 16 weeks
    total_candy_bars_received = candy_bars_per_week * total_weeks

    # L2
    weeks_per_eaten_bar = 4 # every 4 weeks
    eaten_per_period = 1 # eat 1 candy bar
    total_candy_bars_eaten = total_weeks / weeks_per_eaten_bar

    # L3
    candy_bars_saved = total_candy_bars_received - total_candy_bars_eaten

    # FA
    answer = candy_bars_saved
    return answer