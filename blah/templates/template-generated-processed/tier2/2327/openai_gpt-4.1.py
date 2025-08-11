def solve():
    """Index: 2327.
    Returns: her out-of-pocket cost for the seeing-eye dog.
    """
    # L1
    training_cost_per_week = 250 # training costs $250 a week
    training_weeks = 12 # 12 weeks of training
    total_training_cost = training_cost_per_week * training_weeks

    # L2
    certification_cost = 3000 # certification costs $3000
    insurance_coverage_percent = 0.9 # insurance covers 90% of that
    insurance_coverage_amount = certification_cost * insurance_coverage_percent

    # L3
    out_of_pocket_certification = certification_cost - insurance_coverage_amount

    # L4
    adoption_fee = 150 # adoption fee cost $150
    total_cost = adoption_fee + out_of_pocket_certification + total_training_cost

    # FA
    answer = total_cost
    return answer