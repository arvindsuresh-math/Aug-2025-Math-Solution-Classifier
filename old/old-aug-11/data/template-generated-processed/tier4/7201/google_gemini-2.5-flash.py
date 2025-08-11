def solve():
    """Index: 7201.
    Returns: the amount of money the museum gets from college students that are residents of NYC.
    """
    # L1
    total_visitors = 200 # 200 people visit The Metropolitan Museum of Art
    nyc_resident_fraction_divisor = 2 # Half of the visitors are residents of New York City
    nyc_residents = total_visitors / nyc_resident_fraction_divisor

    # L2
    college_student_percent = 0.30 # 30% are college students
    college_students_nyc_residents = nyc_residents * college_student_percent

    # L3
    ticket_cost_college_student = 4 # cost of a college student ticket is $4
    money_from_college_students = college_students_nyc_residents * ticket_cost_college_student

    # FA
    answer = money_from_college_students
    return answer