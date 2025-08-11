def solve():
    """Index: 4428.
    Returns: the total miles traveled across all legs of the trip.
    """
    # L1
    third_leg_distance = 40 # The third point on his trip was 40 miles away
    half_multiplier = 2 # half the distance he traveled from the beginning to his first destination
    first_leg_distance = third_leg_distance * half_multiplier

    # L2
    second_leg_multiplier = 2 # traveled twice the distance to this second destination
    second_leg_distance = first_leg_distance * second_leg_multiplier

    # L3
    # The solution states the fourth leg was equal to the sum of the first 3 legs, despite the question stating 'twice'.
    # We formalize the solution's explicit statement and calculation.
    fourth_leg_distance = third_leg_distance + first_leg_distance + second_leg_distance

    # L4
    total_distance = fourth_leg_distance + fourth_leg_distance

    # FA
    answer = total_distance
    return answer