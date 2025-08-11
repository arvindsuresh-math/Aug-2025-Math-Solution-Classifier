def solve():
    """Index: 717.
    Returns: the amount of pure alcohol Jake drank in ounces.
    """
    # L1
    total_shots = 8 # 8 shots of vodka
    num_people_sharing = 2 # splits ... with his friend
    jake_shots = total_shots / num_people_sharing

    # L2
    ounces_per_shot = 1.5 # Each shot of vodka is 1.5 ounces
    jake_vodka_ounces = jake_shots * ounces_per_shot

    # L3
    alcohol_purity_decimal = 0.5 # 50% pure alcohol
    jake_pure_alcohol_ounces = jake_vodka_ounces * alcohol_purity_decimal

    # FA
    answer = jake_pure_alcohol_ounces
    return answer