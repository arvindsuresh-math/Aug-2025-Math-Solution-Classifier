def solve():
    """Index: 1172.
    Returns: the number of planks Colbert needs to buy from the store.
    """
    # L1
    total_planks_needed = 200 # The treehouse needs 200 wooden planks
    storage_fraction_denominator = 4 # A quarter of these planks
    planks_from_storage = total_planks_needed / storage_fraction_denominator

    # L2
    parents_fraction_denominator = 2 # half of these planks
    planks_from_parents = total_planks_needed / parents_fraction_denominator

    # L3
    planks_from_friends = 20 # 20 planks come from Colbert’s friends
    planks_not_bought = planks_from_storage + planks_from_parents + planks_from_friends

    # L4
    planks_to_buy = total_planks_needed - planks_not_bought

    # FA
    answer = planks_to_buy
    return answer