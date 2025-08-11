def solve():
    """Index: 6648.
    Returns: the total number of pencils Donna and Marcia bought altogether.
    """
    # L1
    cindi_spent = 30 # Cindi spent $30
    pencil_cost = 0.50 # $0.50 pencils
    cindi_pencils = cindi_spent / pencil_cost

    # L2
    marcia_multiplier = 2 # double the number of pencils as Cindi did
    marcia_pencils = marcia_multiplier * cindi_pencils

    # L3
    donna_multiplier = 3 # 3 times as many pencils as Marcia did
    donna_pencils = donna_multiplier * marcia_pencils

    # L4
    total_pencils = marcia_pencils + donna_pencils

    # FA
    answer = total_pencils
    return answer