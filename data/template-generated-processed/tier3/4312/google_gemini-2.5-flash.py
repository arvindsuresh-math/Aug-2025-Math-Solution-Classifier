def solve():
    """Index: 4312.
    Returns: the total number of light bulb packs Sean needs.
    """
    # L1
    bedroom_bulbs = 2 # 2 light bulbs in his bedroom
    bathroom_bulbs = 1 # 1 in both the bathroom
    kitchen_bulbs = 1 # and the kitchen
    basement_bulbs = 4 # and 4 in the basement
    bulbs_bedroom_bathroom_kitchen_basement = bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs

    # L2
    half_divisor = 2 # 1/2 of that amount
    garage_bulbs = bulbs_bedroom_bathroom_kitchen_basement / half_divisor

    # L3
    total_bulbs_needed = bulbs_bedroom_bathroom_kitchen_basement + garage_bulbs

    # L4
    bulbs_per_pack = 2 # The bulbs come 2 per pack
    packs_needed = total_bulbs_needed / bulbs_per_pack

    # FA
    answer = packs_needed
    return answer