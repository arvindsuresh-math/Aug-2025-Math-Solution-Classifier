def solve():
    """Index: 543.
    Returns: the total amount of money the class was able to gather.
    """
    # L1
    full_amount = 50 # pay $50 each
    half_divisor = 2 # paid half
    half_amount = full_amount / half_divisor

    # L2
    students_paid_half = 4 # 4 students, who paid half
    total_from_half_payers = students_paid_half * half_amount

    # L3
    total_students = 25 # 25 students
    students_paid_full = total_students - students_paid_half

    # L4
    total_from_full_payers = students_paid_full * full_amount

    # L5
    total_gathered = total_from_half_payers + total_from_full_payers

    # FA
    answer = total_gathered
    return answer