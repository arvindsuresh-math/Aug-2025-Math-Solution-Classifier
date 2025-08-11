def solve():
    """Index: 5056.
    Returns: the distance from the gym to Anthony's apartment.
    """
    # L1
    distance_to_work = 10 # The distance from Anthony’s apartment to work is 10 miles
    half_divisor = 2 # half the distance
    half_distance_to_work = distance_to_work / half_divisor

    # L2
    additional_distance = 2 # 2 miles more
    distance_to_gym = additional_distance + half_distance_to_work

    # FA
    answer = distance_to_gym
    return answer