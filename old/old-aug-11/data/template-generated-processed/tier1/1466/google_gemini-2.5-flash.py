def solve():
    """Index: 1466.
    Returns: the total number of times the dogs barked.
    """
    # L1
    num_dogs = 2 # 2 dogs
    barks_per_dog_per_minute = 30 # 30 times per minute
    combined_barks_per_minute = num_dogs * barks_per_dog_per_minute

    # L2
    time_in_minutes = 10 # after 10 minutes
    total_barks = combined_barks_per_minute * time_in_minutes

    # FA
    answer = total_barks
    return answer