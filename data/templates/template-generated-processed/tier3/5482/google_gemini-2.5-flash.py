def solve():
    """Index: 5482.
    Returns: the number of glasses of water Rachel should drink on Saturday.
    """
    # L1
    sunday_glasses = 2 # 2 glasses of water on Sunday
    monday_glasses = 4 # 4 glasses of water on Monday
    sunday_monday_glasses = sunday_glasses + monday_glasses

    # L2
    daily_glasses_tue_fri = 3 # 3 glasses of water every day
    num_days_tue_fri = 4 # for the next 4 days
    tue_fri_glasses = daily_glasses_tue_fri * num_days_tue_fri

    # L3
    total_glasses_sun_fri = sunday_monday_glasses + tue_fri_glasses

    # L4
    ounces_per_glass = 10 # One glass of water is 10 ounces of water
    total_ounces_sun_fri = total_glasses_sun_fri * ounces_per_glass

    # L5
    total_ounces_target = 220 # total of 220 ounces of water in the week
    ounces_needed_saturday = total_ounces_target - total_ounces_sun_fri

    # L6
    glasses_needed_saturday = ounces_needed_saturday / ounces_per_glass

    # FA
    answer = glasses_needed_saturday
    return answer