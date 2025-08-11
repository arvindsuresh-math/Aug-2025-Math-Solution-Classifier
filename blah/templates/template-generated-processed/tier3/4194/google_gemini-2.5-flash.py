def solve():
    """Index: 4194.
    Returns: the number of weeks Henry and his brother can spend eating apples.
    """
    # L1
    apples_per_box = 14 # 14 apples
    num_boxes = 3 # 3 boxes of apples
    total_apples = apples_per_box * num_boxes

    # L2
    num_people = 2 # Henry and his brother
    apples_per_person = total_apples / num_people

    # L3
    days_per_week = 7 # 7 days in a week
    weeks_to_consume = apples_per_person / days_per_week

    # FA
    answer = weeks_to_consume
    return answer