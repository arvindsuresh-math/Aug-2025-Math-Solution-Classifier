def solve():
    """Index: 511.
    Returns: the mass of vegetables sold.
    """
    # L1
    carrots_kg = 15 # 15 kg of carrots
    zucchini_kg = 13 # 13 kg of zucchini
    broccoli_kg = 8 # 8 kg of broccoli
    total_vegetables_kg = carrots_kg + zucchini_kg + broccoli_kg

    # L2
    sold_fraction_denominator = 2 # sold only half of them
    sold_vegetables_kg = total_vegetables_kg / sold_fraction_denominator

    # FA
    answer = sold_vegetables_kg
    return answer