from fractions import Fraction

def solve():
    """Index: 4299.
    Returns: the total number of eggs used at the party.
    """
    # L1
    eggs_per_tray = 30 # A tray of eggs has 30 eggs
    kelsey_fraction = Fraction(2, 5) # 2/5 of a tray of eggs
    kelsey_eggs = kelsey_fraction * eggs_per_tray

    # L2
    stephanie_fraction = Fraction(1, 2) # half a tray of eggs
    stephanie_eggs = stephanie_fraction * eggs_per_tray

    # L3
    kelsey_stephanie_combined_eggs = stephanie_eggs + kelsey_eggs

    # L4
    alayah_more_eggs = 40 # 40 more eggs than Kelsey and Stephanie combined
    alayah_eggs = kelsey_stephanie_combined_eggs + alayah_more_eggs

    # L5
    total_eggs_kelsey_stephanie_alayah = alayah_eggs + kelsey_stephanie_combined_eggs

    # L6
    willa_trays = 2 # two trays of eggs
    willa_eggs = willa_trays * eggs_per_tray

    # L7
    total_eggs_at_party = total_eggs_kelsey_stephanie_alayah + willa_eggs

    # FA
    answer = total_eggs_at_party
    return answer