def solve():
    """Index: 4961.
    Returns: the number of students who wore blue lipstick.
    """
    # L1
    total_students = 200 # 200 students attended school that day
    half_divisor = 2 # half of the students
    students_with_lipstick = total_students / half_divisor

    # L2
    quarter_divisor = 4 # one quarter wore red lipstick
    students_with_red_lipstick = students_with_lipstick / quarter_divisor

    # L3
    fifth_divisor = 5 # one-fifth as many students wearing blue lipstick
    students_with_blue_lipstick = students_with_red_lipstick / fifth_divisor

    # FA
    answer = students_with_blue_lipstick
    return answer