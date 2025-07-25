from fractions import Fraction

def solve():
    """Index: 1901.
    Returns: the total amount of time Roger and his friend took to travel.
    """
    # L1
    fraction_covered = Fraction(1, 4) # 1/4 of the total distance
    total_distance = 200 # The total distance between 2 towns is 200 miles
    distance_covered = fraction_covered * total_distance

    # L2
    remaining_distance = total_distance - distance_covered

    # L3
    time_first_part = 1 # taking 1 hour to do so
    speed = distance_covered / time_first_part

    # L4
    time_remaining_distance = remaining_distance / speed

    # L5
    lunch_time = 1 # taking 1 hour and then drove
    total_time = time_remaining_distance + time_first_part + lunch_time

    # FA
    answer = total_time
    return answer