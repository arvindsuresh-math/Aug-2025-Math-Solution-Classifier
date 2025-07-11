def solve():
    """Index: 875.
    Returns: the total cost Jerry pays for the cartridges.
    """
    # L1
    color_cartridge_cost_per_unit = 32 # each color cartridge costs $32
    color_cartridge_count = 3 # three color cartridges
    total_color_cartridge_cost = color_cartridge_cost_per_unit * color_cartridge_count

    # L2
    bw_cartridge_cost_per_unit = 27 # each black-and-white cartridge costs $27
    total_cost = total_color_cartridge_cost + bw_cartridge_cost_per_unit

    # FA
    answer = total_cost
    return answer