def solve():
    """Index: 6341.
    Returns: the number of days ago the ship should have departed.
    """
    # L1
    days_on_water = 21 # navigates for 21 days
    days_in_customs = 4 # last 4 days
    days_to_warehouse = 7 # arrives on the seventh day
    total_lead_time = days_on_water + days_in_customs + days_to_warehouse

    # L2
    days_from_today_expected = 2 # 2 days from today
    days_already_completed = total_lead_time - days_from_today_expected

    # FA
    answer = days_already_completed
    return answer