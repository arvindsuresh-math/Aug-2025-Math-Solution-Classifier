def solve():
    """Index: 6757.
    Returns: the amount of money Jerry gets from the lawsuit.
    """
    # L1
    annual_salary = 50000 # $50,000 annual salary
    years = 30 # for 30 years
    lost_salary_total = annual_salary * years

    # L2
    medical_bills = 200000 # $200,000 in medical bills
    salary_and_medical_damages = lost_salary_total + medical_bills

    # L3
    punitive_multiplier = 3 # triple the medical and salary damages
    punitive_damages = salary_and_medical_damages * punitive_multiplier

    # L4
    total_asked_for = salary_and_medical_damages + punitive_damages

    # L5
    awarded_percentage_num = 80 # 80%
    awarded_percentage_decimal = 0.8 # 80%
    money_awarded = total_asked_for * awarded_percentage_decimal

    # FA
    answer = money_awarded
    return answer