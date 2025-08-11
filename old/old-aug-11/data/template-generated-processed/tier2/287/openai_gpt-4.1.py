def solve():
    """Index: 287.
    Returns: the total amount Bran still needs to pay for tuition after scholarship and part-time job earnings.
    """
    # L1
    tuition_fee = 90 # Bran's tuition fee is $90
    scholarship_percent = 0.30 # scholarship that takes care of 30% of his tuition fee
    scholarship_amount = tuition_fee * scholarship_percent

    # L2
    remaining_after_scholarship = tuition_fee - scholarship_amount

    # L3
    monthly_job_pay = 15 # pays him $15 per month
    months = 3 # pay his tuition fee within 3 months
    total_job_earnings = monthly_job_pay * months

    # L4
    total_remaining = remaining_after_scholarship - total_job_earnings

    # FA
    answer = total_remaining
    return answer