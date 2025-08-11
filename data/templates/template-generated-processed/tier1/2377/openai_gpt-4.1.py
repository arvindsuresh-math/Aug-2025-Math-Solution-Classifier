def solve():
    """Index: 2377.
    Returns: the total dollar value of tickets sold.
    """
    # L1
    student_ticket_price = 6 # $6 for students
    num_students = 20 # 20 students
    student_total = student_ticket_price * num_students

    # L2
    adult_ticket_price = 8 # $8 for adults
    num_adults = 12 # 12 adults
    adult_total = adult_ticket_price * num_adults

    # L3
    total_value = student_total + adult_total

    # FA
    answer = total_value
    return answer