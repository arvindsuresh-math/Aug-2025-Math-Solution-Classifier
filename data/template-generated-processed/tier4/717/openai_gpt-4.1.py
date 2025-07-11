def solve():
    """Index: 717.
    Returns: the amount of pure alcohol Jake drank in ounces.
    """
    # L1
    total_shots = 8 # Jake splits 8 shots of vodka
    num_people = 2 # with his friend
    jake_shots = total_shots / num_people

    # L2
    shot_ounces = 1.5 # Each shot of vodka is 1.5 ounces
    jake_ounces = jake_shots * shot_ounces

    # L3
    alcohol_fraction = 0.5 # vodka is 50% pure alcohol
    pure_alcohol = jake_ounces * alcohol_fraction

    # FA
    answer = pure_alcohol
    return answer