def solve():
    """Index: 5369.
    Returns: the total revenue Matt makes from his plantation.
    """
    # L1
    plantation_side_length = 500 # 500 feet by 500 feet
    plantation_area_sq_feet = plantation_side_length * plantation_side_length

    # L2
    grams_peanuts_per_sq_foot = 50 # 1 square foot of peanuts can make 50 grams of peanuts
    total_grams_peanuts = plantation_area_sq_feet * grams_peanuts_per_sq_foot

    # L3
    grams_pb_from_peanuts = 5 # 5 grams of peanut butter
    grams_peanuts_for_pb = 20 # 20 grams of peanuts to make 5 grams of peanut butter
    total_grams_peanut_butter = total_grams_peanuts * grams_pb_from_peanuts / grams_peanuts_for_pb

    # L4
    grams_per_kg = 1000 # WK
    total_kg_peanut_butter = total_grams_peanut_butter / grams_per_kg

    # L5
    price_per_kg_pb = 10 # 1 kg of peanut butter sells for $10
    total_revenue = total_kg_peanut_butter * price_per_kg_pb

    # FA
    answer = total_revenue
    return answer