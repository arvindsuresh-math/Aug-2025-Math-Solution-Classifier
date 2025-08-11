def solve():
    """Index: 3220.
    Returns: the total amount Tom pays a year for medication and doctor visits.
    """
    # L1
    months_per_year = 12 # WK
    doctor_visit_frequency_months = 6 # every 6 months
    doctor_visits_per_year = months_per_year / doctor_visit_frequency_months

    # L2
    doctor_visit_cost = 400 # a visit to the doctor costs $400
    total_doctor_cost = doctor_visit_cost * doctor_visits_per_year

    # L3
    cost_per_pill = 5 # $5 per pill
    pills_per_day = 2 # 2 pills every day
    daily_pill_cost_before_insurance = cost_per_pill * pills_per_day

    # L4
    insurance_coverage_percent = 0.8 # insurance covers 80% of that cost
    insurance_covered_amount_per_night = daily_pill_cost_before_insurance * insurance_coverage_percent

    # L5
    daily_out_of_pocket_pill_cost = daily_pill_cost_before_insurance - insurance_covered_amount_per_night

    # L6
    days_per_year = 365 # WK
    annual_out_of_pocket_pill_cost = daily_out_of_pocket_pill_cost * days_per_year

    # L7
    total_annual_cost = total_doctor_cost + annual_out_of_pocket_pill_cost

    # FA
    answer = total_annual_cost
    return answer