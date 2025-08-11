def solve():
    """Index: 4913.
    Returns: the difference in participants between 2019 and 2020.
    """
    # L1
    participants_2018 = 150 # number of participants in the 2018 Science Quiz Bowl was 150
    twice_multiplier = 2 # WK
    twice_participants_2018 = participants_2018 * twice_multiplier

    # L2
    more_than_twice = 20 # 20 more than twice the number of participants in 2019
    participants_2019 = twice_participants_2018 + more_than_twice

    # L3
    half_divisor = 2 # WK
    half_participants_2019 = participants_2019 / half_divisor

    # L4
    less_than_half = 40 # 40 less than half the number of participants in 2019
    participants_2020 = half_participants_2019 - less_than_half

    # L5
    difference_2019_2020 = participants_2019 - participants_2020

    # FA
    answer = difference_2019_2020
    return answer