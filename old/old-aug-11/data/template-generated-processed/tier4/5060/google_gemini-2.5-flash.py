def solve():
    """Index: 5060.
    Returns: the total savings from buying ten sets of 2 packs of 500 mL milk.
    """
    # L1
    cost_two_packs = 2.50 # $2.50
    num_packs_in_set = 2 # 2 packs
    price_per_pack_bulk = cost_two_packs / num_packs_in_set

    # L2
    cost_individual_pack = 1.30 # $1.30 each
    savings_per_pack = cost_individual_pack - price_per_pack_bulk

    # L3
    num_sets = 10 # Ten sets
    packs_per_set = 2 # 2 packs
    total_packs_to_buy = num_sets * packs_per_set

    # L4
    total_savings = savings_per_pack * total_packs_to_buy

    # FA
    answer = total_savings
    return answer