def solve():
    """Index: 3982.
    Returns: the total contribution of everyone.
    """
    # L1
    niraj_contribution = 80 # Niraj contributed $80
    brittany_multiplier = 3 # Brittany's contribution is triple Niraj's
    brittany_contribution = niraj_contribution * brittany_multiplier

    # L2
    angela_multiplier = 3 # Angela's contribution is triple Brittany's
    angela_contribution = brittany_contribution * angela_multiplier

    # L3
    total_contribution = niraj_contribution + brittany_contribution + angela_contribution

    # FA
    answer = total_contribution
    return answer