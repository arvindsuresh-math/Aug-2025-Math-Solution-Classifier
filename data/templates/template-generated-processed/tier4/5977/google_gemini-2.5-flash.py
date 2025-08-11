def solve():
    """Index: 5977.
    Returns: the amount each parent has to pay per year.
    """
    # L1
    former_job_salary = 45000 # His former job paid 45,000 per year
    raise_percentage = 0.2 # offered him a 20% raise
    raise_amount = former_job_salary * raise_percentage

    # L2
    new_wage = former_job_salary + raise_amount

    # L3
    num_kids = 9 # 9 kids
    cost_per_parent = new_wage / num_kids

    # FA
    answer = cost_per_parent
    return answer