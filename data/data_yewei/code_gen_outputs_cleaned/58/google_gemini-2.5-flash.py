def solve_58():
    # Total number of students surveyed
    total_students = 60

    # Fraction of students receiving $6 allowance per day
    fraction_allowance_6 = 2/3
    # Fraction of students receiving $4 allowance per day (the rest)
    fraction_allowance_4 = 1 - fraction_allowance_6

    # Daily allowance amounts
    allowance_6_per_day = 6
    allowance_4_per_day = 4

    # Calculate the number of students who receive $6 allowance per day
    num_students_allowance_6 = int(total_students * fraction_allowance_6)

    # Calculate the number of students who receive $4 allowance per day
    num_students_allowance_4 = total_students - num_students_allowance_6

    # Calculate the total allowance for students receiving $6 per day
    total_allowance_6 = num_students_allowance_6 * allowance_6_per_day

    # Calculate the total allowance for students receiving $4 per day
    total_allowance_4 = num_students_allowance_4 * allowance_4_per_day

    # Calculate the total amount of money all 60 students get in a day
    total_daily_allowance = total_allowance_6 + total_allowance_4

    return total_daily_allowance