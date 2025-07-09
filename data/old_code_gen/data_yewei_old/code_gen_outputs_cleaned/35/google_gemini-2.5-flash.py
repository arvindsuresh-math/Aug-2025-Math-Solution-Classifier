def solve():
    total_students = 60
    percentage_below_b = 40

    # Calculate the percentage of students who got B and above
    percentage_b_and_above = 100 - percentage_below_b

    # Calculate the number of students who got B and above
    students_b_and_above = (percentage_b_and_above / 100) * total_students

    return int(students_b_and_above)