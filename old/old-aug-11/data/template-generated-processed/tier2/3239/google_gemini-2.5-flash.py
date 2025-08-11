def solve():
    """Index: 3239.
    Returns: the amount Carl personally owes.
    """
    # L1
    property_damage_cost = 40000 # $40,000 worth of property damage
    medical_bills_cost = 70000 # $70,000 worth of medical bills
    total_cost = property_damage_cost + medical_bills_cost

    # L2
    carl_pay_percentage = 0.2 # leaving Carl to pay the remaining 20%
    carl_personal_cost = total_cost * carl_pay_percentage

    # FA
    answer = carl_personal_cost
    return answer