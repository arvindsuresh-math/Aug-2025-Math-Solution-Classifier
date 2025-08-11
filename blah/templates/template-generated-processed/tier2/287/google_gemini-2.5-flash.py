def solve():
    """Index: 287.
    Returns: the amount Bran still needs to pay for his tuition fee.
    """
    # L1
    tuition_fee = 90 # tuition fee is $90
    scholarship_percent = 0.30 # scholarship that takes care of 30% of his tuition fee
    scholarship_amount = tuition_fee * scholarship_percent

    # L2
    remaining_tuition_after_scholarship = tuition_fee - scholarship_amount

    # L3
    monthly_pay = 15 # pays him $15 per month
    payment_months = 3 # within 3 months
    earnings_from_job = monthly_pay * payment_months

    # L4
    final_amount_to_pay = remaining_tuition_after_scholarship - earnings_from_job

    # FA
    answer = final_amount_to_pay
    return answer