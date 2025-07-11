def solve():
    """Index: 2609.
    Returns: the total number of bracelets Nancy and Rose can make.
    """
    # L1
    metal_beads_nancy = 40 # 40 metal beads
    additional_pearl_beads = 20 # 20 more pearl beads
    pearl_beads_nancy = metal_beads_nancy + additional_pearl_beads

    # L2
    total_beads_nancy = metal_beads_nancy + pearl_beads_nancy

    # L3
    crystal_beads_rose = 20 # 20 crystal beads
    twice_multiplier = 2 # WK
    stone_beads_rose = twice_multiplier * crystal_beads_rose

    # L4
    total_beads_rose = crystal_beads_rose + stone_beads_rose

    # L5
    total_beads_altogether = total_beads_nancy + total_beads_rose

    # L6
    beads_per_bracelet = 8 # eight beads in each bracelet
    total_bracelets = total_beads_altogether / beads_per_bracelet

    # FA
    answer = total_bracelets
    return answer