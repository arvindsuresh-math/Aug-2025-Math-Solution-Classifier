def solve():
    """Index: 4543.
    Returns: the number of students who picked strawberries as their favorite fruit.
    """
    # L1
    students_liked_oranges = 70 # 70 students said they liked oranges
    students_liked_pears = 120 # 120 students said they liked pears
    students_liked_apples = 147 # 147 students said they liked apples
    sum_other_fruits = students_liked_oranges + students_liked_pears + students_liked_apples

    # L2
    total_students_interviewed = 450 # 450 students
    students_liked_strawberries = total_students_interviewed - sum_other_fruits

    # FA
    answer = students_liked_strawberries
    return answer