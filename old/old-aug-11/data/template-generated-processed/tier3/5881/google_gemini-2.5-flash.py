def solve():
    """Index: 5881.
    Returns: the number of gallons of gas John uses a week.
    """
    # L1
    miles_to_work_one_way = 20 # drives 20 miles to work each way
    work_directions = 2 # each way
    daily_work_miles = miles_to_work_one_way * work_directions

    # L2
    work_days_per_week = 5 # 5 days a week
    weekly_work_miles = daily_work_miles * work_days_per_week

    # L3
    leisure_miles_per_week = 40 # another 40 miles a week for leisure travel
    total_miles_per_week = weekly_work_miles + leisure_miles_per_week

    # L4
    car_mpg = 30 # John's car gets 30 mpg
    gallons_used_per_week = total_miles_per_week / car_mpg

    # FA
    answer = gallons_used_per_week
    return answer