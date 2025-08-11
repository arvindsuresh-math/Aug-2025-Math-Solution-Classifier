def solve():
    """Index: 5025.
    Returns: the difference in net dollars one candidate will make the company than the other.
    """
    # L1
    training_cost_per_month = 1200 # costs $1200 a month
    training_months = 3 # 3 months of additional training
    first_candidate_training_cost = training_cost_per_month * training_months

    # L2
    first_candidate_revenue = 93000 # make the company $93000 in the first year
    first_candidate_salary = 42000 # accept a salary of $42000
    first_candidate_net_gain = first_candidate_revenue - first_candidate_salary - first_candidate_training_cost

    # L3
    second_candidate_salary = 45000 # requesting a salary of $45000
    bonus_percentage_numerator = 1 # a hiring bonus of 1% of his salary
    bonus_percentage_denominator = 100 # a hiring bonus of 1% of his salary
    second_candidate_bonus_cost = second_candidate_salary * bonus_percentage_numerator / bonus_percentage_denominator

    # L4
    second_candidate_revenue = 92000 # will make the company $92000 in the first year
    second_candidate_net_gain = second_candidate_revenue - second_candidate_salary - second_candidate_bonus_cost

    # L5
    difference_in_net_gain = first_candidate_net_gain - second_candidate_net_gain

    # FA
    answer = difference_in_net_gain
    return answer