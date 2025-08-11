def solve():
    """Index: 3798.
    Returns: the total amount John pays for the first year.
    """
    # L1
    other_members = 3 # 3 other members of his family
    john = 1 # John joins
    total_members = other_members + john

    # L2
    joining_fee_per_person = 4000 # $4000 per person
    total_joining_cost = total_members * joining_fee_per_person

    # L3
    monthly_cost_per_person = 1000 # $1000 per person
    months_per_year = 12 # WK
    annual_cost_per_person = monthly_cost_per_person * months_per_year

    # L4
    total_annual_cost = annual_cost_per_person * total_members

    # L5
    overall_total_cost = total_joining_cost + total_annual_cost

    # L6
    johns_share_divisor = 2 # John pays half the cost
    johns_payment = overall_total_cost / johns_share_divisor

    # FA
    answer = johns_payment
    return answer