def solve():
    """Index: 5345.
    Returns: the number of months it will take Lee to save enough money for the ring.
    """
    # L1
    annual_salary = 60000 # $60,000 per year in salary
    months_per_year = 12 # WK
    monthly_salary = annual_salary / months_per_year

    # L2
    months_salary_for_ring = 2 # two months' salary
    ring_cost = months_salary_for_ring * monthly_salary

    # L3
    monthly_savings = 1000 # can save $1000 per month
    time_to_save_months = ring_cost / monthly_savings

    # FA
    answer = time_to_save_months
    return answer