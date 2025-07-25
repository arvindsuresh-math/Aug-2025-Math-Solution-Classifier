def solve():
    """Index: 5167.
    Returns: the total number of apples packed in the two weeks.
    """
    # L1
    apples_per_box = 40 # normally pack 40 apples in a box
    full_boxes_per_day = 50 # producing 50 full boxes per day
    apples_packed_per_day_week1 = apples_per_box * full_boxes_per_day

    # L2
    days_in_week = 7 # WK
    total_apples_week1 = apples_packed_per_day_week1 * days_in_week

    # L3
    fewer_apples_per_day_week2 = 500 # packed 500 fewer apples per day
    apples_packed_per_day_week2 = apples_packed_per_day_week1 - fewer_apples_per_day_week2

    # L4
    total_apples_week2 = apples_packed_per_day_week2 * days_in_week

    # L5
    total_apples_two_weeks = total_apples_week1 + total_apples_week2

    # FA
    answer = total_apples_two_weeks
    return answer