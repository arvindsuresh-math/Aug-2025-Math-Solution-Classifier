def solve():
    """Index: 2700.
    Returns: the average number of vegetables each student must eat per school week.
    """
    # L1
    points_needed = 200 # 200 points to win the movie day
    points_per_vegetable = 2 # gives the student 2 points
    total_vegetables_needed = points_needed / points_per_vegetable

    # L2
    num_students = 25 # 25 students in the class
    vegetables_per_student_total = total_vegetables_needed / num_students

    # L3
    num_school_weeks = 2 # two school weeks
    avg_vegetables_per_student_per_week = vegetables_per_student_total / num_school_weeks

    # FA
    answer = avg_vegetables_per_student_per_week
    return answer