def solve():
    """Index: 4883.
    Returns: the amount Tim paid after insurance coverage.
    """
    # L1
    doctor_hourly_rate = 300 # charges $300 per hour
    half_hour_divisor = 2 # WK
    doctor_charge_exam = doctor_hourly_rate / half_hour_divisor

    # L2
    seen_fee = 150 # $150 fee just for being seen
    mri_cost = 1200 # MRI which costs $1200
    total_cost_before_insurance = doctor_charge_exam + seen_fee + mri_cost

    # L3
    insurance_coverage_percent = 0.8 # Insurance covered 80%
    insurance_covered_amount = total_cost_before_insurance * insurance_coverage_percent

    # L4
    amount_paid_by_tim = total_cost_before_insurance - insurance_covered_amount

    # FA
    answer = amount_paid_by_tim
    return answer