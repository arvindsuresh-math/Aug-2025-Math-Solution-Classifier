from fractions import Fraction

def solve():
    """Index: 5796.
    Returns: the size of the raised bed section of the garden.
    """
    # L1
    garden_length = 220 # 220 feet long
    garden_width = 120 # 120 feet wide
    total_garden_area = garden_length * garden_width

    # L2
    half_divisor = 2 # Half of the garden
    remaining_area_for_trellises_and_beds = total_garden_area / half_divisor

    # L3
    trellis_fraction = Fraction(1, 3) # A third of the rest
    whole_fraction = 1 # WK
    raised_bed_fraction_of_remaining = whole_fraction - trellis_fraction

    # L4
    raised_bed_area = remaining_area_for_trellises_and_beds * raised_bed_fraction_of_remaining

    # FA
    answer = raised_bed_area
    return answer