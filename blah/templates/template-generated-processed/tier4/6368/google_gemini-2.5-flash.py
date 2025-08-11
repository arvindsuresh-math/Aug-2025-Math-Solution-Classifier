def solve():
    """Index: 6368.
    Returns: the cost of House A.
    """
    # L1
    total_earnings = 8000 # earns $8,000 total
    base_salary = 3000 # base salary of $3,000 a month
    commission_earnings = total_earnings - base_salary

    # L2
    commission_rate = 0.02 # 2% commission
    total_houses_cost = commission_earnings / commission_rate

    # L5
    house_b_multiplier = 3 # House B costs three times as much as House A
    house_c_multiplier = 2 # House C cost twice as much as House A
    house_c_deduction = 110000 # minus $110,000
    combined_a_coefficient = 1 + house_b_multiplier + house_c_multiplier

    # L6
    rhs_after_addition = total_houses_cost + house_c_deduction

    # L7
    house_a_cost = rhs_after_addition / combined_a_coefficient

    # FA
    answer = house_a_cost
    return answer