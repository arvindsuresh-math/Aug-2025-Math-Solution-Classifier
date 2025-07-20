def solve():
    """Index: 5317.
    Returns: the amount the husband still needs to pay.
    """
    # L1
    medical_procedure_cost = 128 # which cost her $128
    couple_share_divisor = 2 # pay half of the medical expenses
    couple_covered_medical_expense = medical_procedure_cost / couple_share_divisor

    # L2
    house_help_salary = 160 # her $160 salary
    total_couple_expense = house_help_salary + couple_covered_medical_expense

    # L3
    equal_split_divisor = 2 # split their expenses equally
    each_person_share = total_couple_expense / equal_split_divisor

    # L4
    husband_remaining_payment = each_person_share - couple_covered_medical_expense

    # FA
    answer = husband_remaining_payment
    return answer