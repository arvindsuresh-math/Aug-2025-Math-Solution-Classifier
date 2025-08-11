def solve():
    """Index: 6090.
    Returns: the total amount the gym makes a month.
    """
    # L1
    charge_per_instance = 18 # $18 twice a month
    times_charged_per_month = 2 # twice a month
    charge_per_person_per_month = charge_per_instance * times_charged_per_month

    # L2
    num_members = 300 # 300 members
    total_monthly_income = charge_per_person_per_month * num_members

    # FA
    answer = total_monthly_income
    return answer