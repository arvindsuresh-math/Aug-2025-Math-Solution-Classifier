def solve():
    """Index: 5426.
    Returns: the total number of chickens after 9 years.
    """
    # L1
    annual_increase = 150 # 150 chickens annually
    num_years = 9 # after 9 years
    total_increase = annual_increase * num_years

    # L2
    current_chickens = 550 # 550
    final_chickens = current_chickens + total_increase

    # FA
    answer = final_chickens
    return answer