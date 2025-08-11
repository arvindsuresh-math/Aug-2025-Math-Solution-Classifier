def solve():
    """Index: 3069.
    Returns: Marianne's age when Bella turns 18.
    """
    # L1
    marianne_initial_age = 20 # Marianne was 20 years old
    bella_initial_age = 8 # Bella was 8 years old
    age_difference = marianne_initial_age - bella_initial_age

    # L2
    bella_target_age = 18 # Bella turns 18
    years_to_add = bella_target_age - bella_initial_age

    # L3
    marianne_final_age = marianne_initial_age + years_to_add

    # FA
    answer = marianne_final_age
    return answer