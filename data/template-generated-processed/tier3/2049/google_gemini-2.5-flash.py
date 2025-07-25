def solve():
    """Index: 2049.
    Returns: the difference in time Mark spends walking compared to Chris.
    """
    # L1
    distance_walked_back_home = 3 # After walking 3 miles Mark has to turn around and go home
    multiplier_for_round_trip = 2 # multiplying the distance he walks back to the house by 2
    distance_to_get_lunch = distance_walked_back_home * multiplier_for_round_trip

    # L2
    distance_house_to_school = 9 # If the distance from their house to the school is 9 miles
    total_distance_mark_walks = distance_to_get_lunch + distance_house_to_school

    # L3
    speed = 3 # who walks 3 miles per hour
    time_mark_walks = total_distance_mark_walks / speed

    # L4
    time_chris_walks = distance_house_to_school / speed

    # L5
    time_difference = time_mark_walks - time_chris_walks

    # FA
    answer = time_difference
    return answer