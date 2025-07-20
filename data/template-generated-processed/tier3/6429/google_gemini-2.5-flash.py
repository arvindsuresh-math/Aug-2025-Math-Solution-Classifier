def solve():
    """Index: 6429.
    Returns: the total grams of protein Arnold will consume.
    """
    # L1
    collagen_protein_for_two_scoops = 18 # 18 grams of protein for every 2 scoops
    collagen_scoops_per_serving = 2 # 2 scoops
    collagen_protein_consumed = collagen_protein_for_two_scoops / collagen_scoops_per_serving

    # L2
    protein_powder_grams_per_scoop = 21 # 21 grams of protein per scoop
    steak_protein_grams = 56 # 56 grams of protein
    total_protein_consumed = collagen_protein_consumed + protein_powder_grams_per_scoop + steak_protein_grams

    # FA
    answer = total_protein_consumed
    return answer