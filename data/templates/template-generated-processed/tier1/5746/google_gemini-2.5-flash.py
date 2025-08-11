def solve():
    """Index: 5746.
    Returns: the total cost of the museum tickets.
    """
    # L1
    num_students = 12 # 12 archeology students
    student_ticket_cost = 1 # Student tickets cost $1 each
    cost_student_tickets = num_students * student_ticket_cost

    # L2
    num_teachers = 4 # 4 teachers
    adult_ticket_cost = 3 # adult tickets cost $3 each
    cost_teacher_tickets = num_teachers * adult_ticket_cost

    # L3
    total_cost = cost_student_tickets + cost_teacher_tickets

    # FA
    answer = total_cost
    return answer