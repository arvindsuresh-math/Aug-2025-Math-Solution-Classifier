def solve():
    """Index: 2606.
    Returns: the total cost the school will pay for the farm entrance.
    """
    # L1
    student_fee_per_person = 5 # farm entrance fee for students costs $5
    num_students = 35 # all 35 students in the class
    total_student_fee = student_fee_per_person * num_students

    # L2
    adult_fee_per_person = 6 # $6 for adults
    num_adults = 4 # 4 adult chaperones
    total_adult_fee = adult_fee_per_person * num_adults

    # L3
    total_entrance_fee = total_student_fee + total_adult_fee

    # FA
    answer = total_entrance_fee
    return answer