from fractions import Fraction

def solve():
    """Index: 6104.
    Returns: the average time the two take to complete the race.
    """
    # L1
    longer_fraction = Fraction(1, 3) # 1/3 times longer
    casey_time = 6 # Casey takes 6 hours
    zendaya_extra_time = longer_fraction * casey_time

    # L2
    zendaya_total_time = casey_time + zendaya_extra_time

    # L3
    combined_time = zendaya_total_time + casey_time

    # L4
    number_of_people = 2 # WK
    average_time = combined_time / number_of_people

    # FA
    answer = average_time
    return answer