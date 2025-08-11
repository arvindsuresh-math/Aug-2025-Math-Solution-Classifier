def solve():
    """Index: 1739.
    Returns: the number of students that can go on the field trip.
    """
    # L1
    budget = 350 # budget of $350
    bus_cost = 100 # cost to rent a school bus is $100
    available_for_admission = budget - bus_cost

    # L2
    admission_cost_per_student = 10 # cost of admission is $10 per student
    num_students = available_for_admission / admission_cost_per_student

    # FA
    answer = num_students
    return answer