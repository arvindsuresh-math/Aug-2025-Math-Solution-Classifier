def solve():
    """Index: 1836.
    Returns: the number of more candies Andy has than Caleb.
    """
    # L1
    billy_initial_candies = 6 # Billy took 6 candies with him
    father_gave_billy = 8 # He gave 8 candies to Billy
    billy_total_candies = billy_initial_candies + father_gave_billy

    # L2
    caleb_initial_candies = 11 # Caleb took 11
    father_gave_caleb = 11 # 11 to Caleb
    caleb_total_candies = caleb_initial_candies + father_gave_caleb

    # L3
    total_packet_candies = 36 # a packet of 36 candies
    father_given_out = father_gave_billy + father_gave_caleb

    # L4
    father_gave_andy = total_packet_candies - father_given_out

    # L5
    andy_initial_candies = 9 # Andy left with 9
    andy_total_candies = andy_initial_candies + father_gave_andy

    # L6
    andy_more_than_caleb = andy_total_candies - caleb_total_candies

    # FA
    answer = andy_more_than_caleb
    return answer