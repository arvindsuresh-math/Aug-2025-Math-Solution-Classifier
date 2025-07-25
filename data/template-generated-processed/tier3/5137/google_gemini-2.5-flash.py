def solve():
    """Index: 5137.
    Returns: the number of buses needed for the field trip.
    """
    # L1
    fifth_graders = 109 # 109 fifth graders
    sixth_graders = 115 # 115 sixth graders
    seventh_graders = 118 # 118 seventh graders
    total_students = fifth_graders + sixth_graders + seventh_graders

    # L2
    teachers_per_grade = 4 # 4 teachers
    parents_per_grade = 2 # 2 parents from each grade
    adults_per_grade = teachers_per_grade + parents_per_grade

    # L3
    number_of_grades = 3 # 109 fifth graders, 115 sixth graders, and 118 seventh graders
    total_adults = number_of_grades * adults_per_grade

    # L4
    total_people = total_students + total_adults

    # L5
    seats_per_bus = 72 # 72 seats on each school bus
    buses_needed = total_people / seats_per_bus

    # FA
    answer = buses_needed
    return answer