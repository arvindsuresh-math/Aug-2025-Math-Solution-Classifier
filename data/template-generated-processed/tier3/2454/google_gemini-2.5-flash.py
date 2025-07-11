def solve():
    """Index: 2454.
    Returns: the difference in students wearing striped shirts and shorts.
    """
    # L1
    total_students = 81 # In a classroom of 81 students
    denominator_checkered = 3 # two-thirds are wearing striped shirts while the others are wearing checkered shirts
    checkered_shirts = total_students / denominator_checkered

    # L2
    numerator_striped = 2 # two-thirds are wearing striped shirts
    striped_shirts = checkered_shirts * numerator_striped

    # L3
    more_shorts_than_checkered = 19 # 19 more students wearing shorts than checkered shirts
    students_wearing_shorts = checkered_shirts + more_shorts_than_checkered

    # L4
    difference_striped_shorts = striped_shirts - students_wearing_shorts

    # FA
    answer = difference_striped_shorts
    return answer