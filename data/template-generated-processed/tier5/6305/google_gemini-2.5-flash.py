def solve():
    """Index: 6305.
    Returns: the number of donuts Gamma received.
    """
    # L2
    total_donuts_initial = 40 # Delta, Beta and Gamma decided to share 40 donuts
    delta_donuts = 8 # Delta took 8 donuts
    donuts_for_beta_gamma = total_donuts_initial - delta_donuts

    # L6
    # Beta took three times as many as Gamma (3x), and Gamma took x, so total is 4x.
    division_coefficient = 4 # from 4x = 32, dividing by 4
    gamma_donuts = donuts_for_beta_gamma / division_coefficient

    # FA
    answer = gamma_donuts
    return answer