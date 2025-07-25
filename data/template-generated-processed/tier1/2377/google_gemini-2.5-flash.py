def solve():
    """Index: 2377.
    Returns: the total dollars' worth of tickets sold.
    """
    # L1
    student_ticket_cost = 6 # $6 for students
    num_students = 20 # 20 students
    student_ticket_total = student_ticket_cost * num_students

    # L2
    adult_ticket_cost = 8 # $8 for adults
    num_adults = 12 # 12 adults
    adult_ticket_total = adult_ticket_cost * num_adults

    # L3
    total_tickets_sold = student_ticket_total + adult_ticket_total

    # FA
    answer = total_tickets_sold
    return answer