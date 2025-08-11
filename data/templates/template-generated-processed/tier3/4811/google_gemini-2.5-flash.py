def solve():
    """Index: 4811.
    Returns: the number of people with green eyes.
    """
    # L1
    total_people = 100 # 100 people in a theater
    brown_eyes_divisor = 2 # half of them have brown eyes
    brown_eyes_people = total_people / brown_eyes_divisor

    # L2
    black_eyes_divisor = 4 # a quarter have black eyes
    black_eyes_people = total_people / black_eyes_divisor

    # L3
    blue_eyes_people = 19 # 19 of these people have blue eyes
    sum_other_eyes = brown_eyes_people + black_eyes_people + blue_eyes_people

    # L4
    green_eyes_people = total_people - sum_other_eyes

    # FA
    answer = green_eyes_people
    return answer