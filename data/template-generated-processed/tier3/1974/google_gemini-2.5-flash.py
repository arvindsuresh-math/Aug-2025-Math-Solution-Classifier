def solve():
    """Index: 1974.
    Returns: the percentage increase in Kathleen's weekly allowance.
    """
    # L1
    base_allowance_middle_school = 8 # $8
    additional_allowance_middle_school = 2 # $2 more than $8
    middle_school_allowance = base_allowance_middle_school + additional_allowance_middle_school

    # L2
    twice_multiplier = 2 # WK
    twice_middle_school_allowance = middle_school_allowance * twice_multiplier

    # L3
    additional_allowance_senior_year = 5 # $5 more than twice her middle school allowance
    senior_year_allowance = twice_middle_school_allowance + additional_allowance_senior_year

    # L4
    allowance_increase_amount = senior_year_allowance - middle_school_allowance

    # L5
    percentage_multiplier = 100 # WK
    percentage_increase = (allowance_increase_amount / middle_school_allowance) * percentage_multiplier

    # FA
    answer = percentage_increase
    return answer