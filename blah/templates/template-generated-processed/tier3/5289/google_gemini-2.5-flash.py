def solve():
    """Index: 5289.
    Returns: the total amount of money John made from recycling.
    """
    # L1
    days_in_week = 7 # WK
    sunday_days = 1 # WK
    monday_saturday_paper_weight_ounces = 8 # The Monday-Saturday papers weigh 8 ounces each.
    non_sunday_days = days_in_week - sunday_days

    # L2
    non_sunday_weekly_weight_ounces = non_sunday_days * monday_saturday_paper_weight_ounces

    # L3
    sunday_paper_weight_multiplier = 2 # The Sunday paper weighs twice as much.
    sunday_paper_weight_ounces = monday_saturday_paper_weight_ounces * sunday_paper_weight_multiplier
    total_weekly_paper_weight_ounces = non_sunday_weekly_weight_ounces + sunday_paper_weight_ounces

    # L4
    ounces_per_pound = 16 # WK
    total_weekly_paper_weight_pounds = total_weekly_paper_weight_ounces / ounces_per_pound

    # L5
    papers_per_day = 250 # He is supposed to deliver 250 papers a day.
    weekly_delivery_weight_pounds = total_weekly_paper_weight_pounds * papers_per_day

    # L6
    number_of_weeks = 10 # He doesn't deliver them for 10 weeks.
    total_pounds_delivered = weekly_delivery_weight_pounds * number_of_weeks

    # L7
    pounds_per_ton = 2000 # WK
    total_tons_delivered = total_pounds_delivered / pounds_per_ton

    # L8
    price_per_ton = 20 # If one ton of paper recycles for $20
    total_money_made = total_tons_delivered * price_per_ton

    # FA
    answer = total_money_made
    return answer