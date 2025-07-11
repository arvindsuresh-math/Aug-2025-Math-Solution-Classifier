def solve():
    """Index: 229.
    Returns: the number of cable sections Jan keeps on hand.
    """
    # L1
    total_cable_length = 1000 # Jan buys 1000 feet of cable
    section_length = 25 # splits it up into 25-foot sections
    total_sections = total_cable_length / section_length

    # L2
    give_fraction_denominator = 4 # gives 1/4 of that to a friend
    sections_given = total_sections / give_fraction_denominator

    # L3
    sections_after_giving = total_sections - sections_given

    # L4
    storage_divisor = 2 # puts half of the rest in storage
    sections_on_hand = sections_after_giving / storage_divisor

    # FA
    answer = sections_on_hand
    return answer