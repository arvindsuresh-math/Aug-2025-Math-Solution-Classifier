def solve():
    """Index: 1836.
    Returns: how many more candies Andy now has than Caleb.
    """
    # L1
    billy_initial = 6 # Billy took 6 candies with him
    billy_from_father = 8 # He gave 8 candies to Billy
    billy_total = billy_initial + billy_from_father

    # L2
    caleb_initial = 11 # Caleb took 11
    caleb_from_father = 11 # He gave 11 to Caleb
    caleb_total = caleb_initial + caleb_from_father

    # L3
    # (no new variables needed, but for clarity)
    candies_given_to_billy = billy_from_father
    candies_given_to_caleb = caleb_from_father
    total_given = candies_given_to_billy + candies_given_to_caleb

    # L4
    father_packet = 36 # a packet of 36 candies
    andy_from_father = father_packet - total_given

    # L5
    andy_initial = 9 # Andy left with 9
    andy_total = andy_initial + andy_from_father

    # L6
    difference_andy_caleb = andy_total - caleb_total

    # FA
    answer = difference_andy_caleb
    return answer