def solve():
    """Index: 5986.
    Returns: the required hourly wage for Nancy.
    """
    # L1
    total_tuition = 22000 # The tuition costs $22,000 per semester
    parents_share_divisor = 2 # Her parents can pay half the cost
    remaining_tuition_after_parents = total_tuition / parents_share_divisor

    # L2
    scholarship_amount = 3000 # a scholarship for $3,000
    loan_multiplier = 2 # a student loan for twice her scholarship amount
    student_loan_amount = scholarship_amount * loan_multiplier

    # L3
    tuition_to_pay_by_working = remaining_tuition_after_parents - scholarship_amount - student_loan_amount

    # L4
    total_work_hours = 200 # work a total of 200 hours during the semester
    hourly_wage_needed = tuition_to_pay_by_working / total_work_hours

    # FA
    answer = hourly_wage_needed
    return answer