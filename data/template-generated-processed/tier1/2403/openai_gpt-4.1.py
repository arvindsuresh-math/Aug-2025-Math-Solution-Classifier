def solve():
    """Index: 2403.
    Returns: the total distance the two friends bike in a week.
    """
    # L1
    onur_daily_km = 250 # Onur bikes 250 kilometers a day
    days_per_week = 5 # Five times a week
    onur_weekly_km = days_per_week * onur_daily_km

    # L2
    hanil_more_km = 40 # Hanil bikes 40 more kilometers of Onur biking distance in a day
    hanil_daily_km = onur_daily_km + hanil_more_km

    # L3
    hanil_weekly_km = hanil_daily_km * days_per_week

    # L4
    total_km = hanil_weekly_km + onur_weekly_km

    # FA
    answer = total_km
    return answer