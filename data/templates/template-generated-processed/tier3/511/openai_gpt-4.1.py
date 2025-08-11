def solve():
    """Index: 511.
    Returns: the mass of vegetables the merchant sold in kg.
    """
    # L1
    carrots_kg = 15 # 15 kg of carrots
    zucchini_kg = 13 # 13 kg of zucchini
    broccoli_kg = 8 # 8 kg of broccoli
    total_kg = carrots_kg + zucchini_kg + broccoli_kg

    # L2
    sold_fraction = 2 # sold only half of them
    sold_kg = total_kg / sold_fraction

    # FA
    answer = sold_kg
    return answer