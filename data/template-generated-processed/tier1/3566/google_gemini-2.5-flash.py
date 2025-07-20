def solve():
    """Index: 3566.
    Returns: the number of students who don't eat lunch.
    """
    # L1
    multiplier_thrice = 3 # thrice the number
    students_eat_cafeteria = 10 # 10 students eat in the school cafeteria
    students_bring_lunch = multiplier_thrice * students_eat_cafeteria

    # L2
    total_students_eat_lunch = students_eat_cafeteria + students_bring_lunch

    # L3
    total_students_in_class = 60 # class has 60 students
    students_dont_eat_lunch = total_students_in_class - total_students_eat_lunch

    # FA
    answer = students_dont_eat_lunch
    return answer