def solve():
    """Index: 875.
    Returns: the total amount Jerry pays for all cartridges.
    """
    # L1
    color_cartridge_cost = 32 # each color cartridge costs $32
    num_color_cartridges = 3 # three color cartridges
    total_color_cost = color_cartridge_cost * num_color_cartridges

    # L2
    bw_cartridge_cost = 27 # each black-and-white cartridge costs $27
    total_cost = total_color_cost + bw_cartridge_cost

    # FA
    answer = total_cost
    return answer