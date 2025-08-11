def solve():
    """Index: 6185.
    Returns: the total number of products produced by the factory in 5 days.
    """
    # L1
    refrigerators_per_hour = 90 # 90 refrigerators per hour
    more_coolers_than_refrigerators = 70 # 70 more coolers than refrigerators per hour
    coolers_per_hour = refrigerators_per_hour + more_coolers_than_refrigerators

    # L2
    num_days = 5 # for 5 days
    hours_per_day = 9 # works 9 hours a day
    total_hours_worked = num_days * hours_per_day

    # L3
    total_products_5_days = (refrigerators_per_hour + coolers_per_hour) * total_hours_worked

    # FA
    answer = total_products_5_days
    return answer