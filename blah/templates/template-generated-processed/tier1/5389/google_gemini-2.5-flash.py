def solve():
    """Index: 5389.
    Returns: the total time in seconds Nissa spends grooming her cat.
    """
    # L1
    claws_per_foot = 4 # four claws on each foot
    num_feet = 4 # cat has four feet
    total_claws = claws_per_foot * num_feet

    # L2
    time_per_claw = 10 # 10 seconds to clip each of her cats' nails
    time_clipping_claws = total_claws * time_per_claw

    # L3
    time_per_ear = 90 # 90 seconds to clean each of her ears
    num_ears = 2 # WK
    time_cleaning_ears = time_per_ear * num_ears

    # L4
    shampoo_minutes = 5 # 5 minutes to shampoo her
    seconds_per_minute = 60 # WK
    time_shampooing_seconds = shampoo_minutes * seconds_per_minute

    # L5
    total_grooming_time = time_clipping_claws + time_cleaning_ears + time_shampooing_seconds

    # FA
    answer = total_grooming_time
    return answer