def solve():
    """Index: 4111.
    Returns: the mass of apples that Ali has left.
    """
    # L1
    kidney_apples_kg = 23 # 23 kg of kidney apples
    golden_apples_kg = 37 # 37 kg of golden apples
    canada_apples_kg = 14 # 14 kg of Canada apples
    total_initial_apples_kg = kidney_apples_kg + golden_apples_kg + canada_apples_kg

    # L2
    sold_apples_kg = 36 # 36 kg of apples were sold
    remaining_apples_kg = total_initial_apples_kg - sold_apples_kg

    # FA
    answer = remaining_apples_kg
    return answer