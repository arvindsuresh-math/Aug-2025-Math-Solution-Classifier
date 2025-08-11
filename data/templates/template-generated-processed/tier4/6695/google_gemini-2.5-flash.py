def solve():
    """Index: 6695.
    Returns: the amount Amanda would save by buying lighters online instead of at the gas station.
    """
    # L1
    total_lighters_needed = 24 # buying 24 lighters
    lighters_per_pack = 12 # per pack of twelve
    num_packs = total_lighters_needed / lighters_per_pack

    # L2
    cost_per_pack_amazon = 5.00 # $5.00 per pack of twelve on Amazon
    total_cost_amazon = num_packs * cost_per_pack_amazon

    # L3
    cost_per_lighter_gas_station = 1.75 # $1.75 each at the gas station
    total_cost_gas_station = total_lighters_needed * cost_per_lighter_gas_station

    # L4
    savings = total_cost_gas_station - total_cost_amazon

    # FA
    answer = savings
    return answer