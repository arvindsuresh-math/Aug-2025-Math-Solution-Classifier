from fractions import Fraction

def solve():
    """Index: 2507.
    Returns: the total distance of the race.
    """
    # L1
    sadie_speed = 3 # 3 miles per hour
    sadie_time = 2 # 2 hours
    sadie_distance = sadie_speed * sadie_time

    # L2
    ariana_speed = 6 # 6 miles per hour
    ariana_time_fraction = Fraction(1, 2) # half an hour
    ariana_distance = ariana_speed * ariana_time_fraction

    # L3
    total_race_time = 4.5 # four and half hours
    ariana_time_decimal = 0.5 # half an hour
    sarah_time = total_race_time - sadie_time - ariana_time_decimal

    # L4
    sarah_speed = 4 # four miles per hour
    sarah_distance = sarah_speed * sarah_time

    # L5
    total_distance = sadie_distance + ariana_distance + sarah_distance

    # FA
    answer = total_distance
    return answer