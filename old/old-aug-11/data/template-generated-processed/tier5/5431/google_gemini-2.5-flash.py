def solve():
    """Index: 5431.
    Returns: the number of gallons Felicity used.
    """
    # L4
    total_gallons = 30 # Together the girls used 30 gallons of gas
    felicity_less_gallons = 5 # 5 less gallons of gas
    adhira_multiplier = 1 # WK
    felicity_multiplier = 4 # four times the number of gallons
    coefficient_of_A = adhira_multiplier + felicity_multiplier
    rhs_after_addition = total_gallons + felicity_less_gallons

    # L5
    adhira_gallons = rhs_after_addition / coefficient_of_A

    # L6
    felicity_gallons = felicity_multiplier * adhira_gallons - felicity_less_gallons

    # FA
    answer = felicity_gallons
    return answer