def solve():
    """Index: 2284.
    Returns: the number of students in the third dance studio.
    """
    # L1
    first_studio = 110 # first two have 110 ... students
    second_studio = 135 # ... and 135 students
    first_two_total = first_studio + second_studio

    # L2
    total_students = 376 # Three local dance studios have 376 students
    third_studio = total_students - first_two_total

    # FA
    answer = third_studio
    return answer