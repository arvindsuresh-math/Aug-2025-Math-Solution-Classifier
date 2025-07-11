def solve():
    """Index: 1890.
    Returns: the total number of towels Jane, Kyla, and Anthony can fold in one hour.
    """
    # L1
    hours_to_consider = 1 # in one hour
    minutes_per_hour = 60 # 60 minutes in 1 hour
    total_minutes_in_hour = hours_to_consider * minutes_per_hour

    # L2
    jane_time_per_set = 5 # Jane can fold 3 towels in 5 minutes
    jane_sets_per_hour = total_minutes_in_hour / jane_time_per_set

    # L3
    jane_towels_per_set = 3 # Jane can fold 3 towels in 5 minutes
    jane_towels_per_hour = jane_towels_per_set * jane_sets_per_hour

    # L4
    kyla_time_per_set = 10 # Kyla can fold 5 towels in 10 minutes
    kyla_sets_per_hour = total_minutes_in_hour / kyla_time_per_set

    # L5
    kyla_towels_per_set = 5 # Kyla can fold 5 towels in 10 minutes
    kyla_towels_per_hour = kyla_towels_per_set * kyla_sets_per_hour

    # L6
    anthony_time_per_set = 20 # Anthony can fold 7 towels in 20 minutes
    anthony_sets_per_hour = total_minutes_in_hour / anthony_time_per_set

    # L7
    anthony_towels_per_set = 7 # Anthony can fold 7 towels in 20 minutes
    anthony_towels_per_hour = anthony_towels_per_set * anthony_sets_per_hour

    # L8
    total_towels_per_hour = jane_towels_per_hour + kyla_towels_per_hour + anthony_towels_per_hour

    # FA
    answer = total_towels_per_hour
    return answer