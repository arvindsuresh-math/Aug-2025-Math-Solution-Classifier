def solve():
    """Index: 7080.
    Returns: the total money Hallie earns from Monday to Wednesday.
    """
    # L1
    hours_monday = 7 # works for 7 hours
    hours_tuesday = 5 # works for 5 hours
    hours_wednesday = 7 # works for 7 hours
    total_hours_worked = hours_monday + hours_tuesday + hours_wednesday

    # L2
    hourly_rate = 10 # $10/hour
    hourly_pay = total_hours_worked * hourly_rate

    # L3
    tips_monday = 18 # $18 in tips
    tips_tuesday = 12 # $12 in tips
    tips_wednesday = 20 # $20 in tips
    total_tips = tips_monday + tips_tuesday + tips_wednesday

    # L4
    total_earnings = hourly_pay + total_tips

    # FA
    answer = total_earnings
    return answer