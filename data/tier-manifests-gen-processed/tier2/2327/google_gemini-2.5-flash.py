def solve():
    """Index: 2327.
    Returns: the total out-of-pocket cost for the seeing-eye dog.
    """
    # L1
    cost_per_week_training = 250 # costs $250 a week
    training_weeks = 12 # 12 weeks of training
    total_training_cost = cost_per_week_training * training_weeks

    # L2
    certification_full_cost = 3000 # certification which costs $3000
    insurance_coverage_rate = 0.9 # insurance covers 90%
    insurance_covered_amount = certification_full_cost * insurance_coverage_rate

    # L3
    out_of_pocket_certification_cost = certification_full_cost - insurance_covered_amount

    # L4
    adoption_fee = 150 # adoption fee cost $150
    total_out_of_pocket_cost = adoption_fee + out_of_pocket_certification_cost + total_training_cost

    # FA
    answer = total_out_of_pocket_cost
    return answer