from fractions import Fraction

def solve():
    """Index: 6562.
    Returns: the total cost of Maciek's purchases.
    """
    # L1
    chip_price_increase_percentage = Fraction(75, 100) # 75% more expensive
    pretzel_cost_per_pack = 4 # A pack of pretzels costs $4
    additional_chip_cost = chip_price_increase_percentage * pretzel_cost_per_pack

    # L2
    chip_cost_per_pack = pretzel_cost_per_pack + additional_chip_cost

    # L3
    num_pretzel_packs = 2 # bought two packets of pretzels
    total_pretzel_cost = pretzel_cost_per_pack * num_pretzel_packs

    # L4
    num_chip_packs = 2 # bought two packets of chips
    total_chip_cost = chip_cost_per_pack * num_chip_packs

    # L5
    total_cost = total_pretzel_cost + total_chip_cost

    # FA
    answer = total_cost
    return answer