def solve():
    """Index: 5709.
    Returns: the total number of cloves of garlic needed.
    """
    # L1
    num_vampires_to_repel = 30 # 30 vampires
    cloves_per_repel_unit = 3 # 3 cloves of garlic
    vampires_per_repel_unit = 2 # 2 vampires
    cloves_for_vampires = num_vampires_to_repel * cloves_per_repel_unit / vampires_per_repel_unit

    # L2
    num_wights_to_repel = 12 # 12 wights
    wights_per_repel_unit = 3 # 3 wights
    cloves_for_wights = num_wights_to_repel * cloves_per_repel_unit / wights_per_repel_unit

    # L3
    num_bats_to_repel = 40 # 40 vampire bats
    bats_per_repel_unit = 8 # 8 vampire bats
    cloves_for_bats = num_bats_to_repel * cloves_per_repel_unit / bats_per_repel_unit

    # L4
    total_cloves = cloves_for_vampires + cloves_for_wights + cloves_for_bats

    # FA
    answer = total_cloves
    return answer