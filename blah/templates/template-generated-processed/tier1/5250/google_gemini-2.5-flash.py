def solve():
    """Index: 5250.
    Returns: the number of people wearing vertical stripes.
    """
    # L1
    total_people = 40 # 40 people in a cafeteria
    checkered_shirts = 7 # 7 out of 40 people in a cafeteria are wearing checkered shirts
    people_wearing_stripes = total_people - checkered_shirts

    # L2
    multiplier_horizontal_checkered = 4 # 4 times as many as the people wearing checkered shirts
    horizontal_stripes = multiplier_horizontal_checkered * checkered_shirts

    # L3
    vertical_stripes = people_wearing_stripes - horizontal_stripes

    # FA
    answer = vertical_stripes
    return answer