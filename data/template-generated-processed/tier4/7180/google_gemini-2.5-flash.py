def solve():
    """Index: 7180.
    Returns: the total cost for Fred to buy enough sodas.
    """
    # L1
    sodas_per_guest = 2 # 2 sodas
    num_guests = 15 # 15 people to the party
    total_cans_needed = sodas_per_guest * num_guests

    # L2
    cans_per_pack = 6 # 6 pack of canned sodas
    num_packs_needed = total_cans_needed / cans_per_pack

    # L3
    cost_per_pack = 3.00 # $3.00
    total_cost = cost_per_pack * num_packs_needed

    # FA
    answer = total_cost
    return answer