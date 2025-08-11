def solve():
    """Index: 2187.
    Returns: the increase in the average age of the students.
    """
    # L1
    num_students_initial = 9 # 9 students
    average_age_initial = 8 # average age of 9 of them is 8 years
    sum_ages_initial = num_students_initial * average_age_initial

    # L2
    age_tenth_student = 28 # the tenth student is (quite strangely) 28 years old
    sum_ages_new = sum_ages_initial + age_tenth_student

    # L3
    total_students_new = 10 # 10 students in a class
    average_age_new = sum_ages_new / total_students_new

    # L4
    increase_in_average = average_age_new - average_age_initial

    # FA
    answer = increase_in_average
    return answer