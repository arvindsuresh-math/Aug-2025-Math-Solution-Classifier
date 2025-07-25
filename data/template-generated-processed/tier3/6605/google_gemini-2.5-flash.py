def solve():
    """Index: 6605.
    Returns: the number of months Rita needs to fulfill her coach's requirements.
    """
    # L1
    backstroke_hours = 50 # 50 hours of backstroke
    breaststroke_hours = 9 # 9 hours of breaststroke
    butterfly_hours = 121 # 121 hours of butterfly
    completed_hours = backstroke_hours + breaststroke_hours + butterfly_hours

    # L2
    total_required_hours = 1500 # a total of 1,500 hours
    remaining_hours = total_required_hours - completed_hours

    # L3
    hours_per_month = 220 # 220 hours every month
    months_needed = remaining_hours / hours_per_month

    # FA
    answer = months_needed
    return answer