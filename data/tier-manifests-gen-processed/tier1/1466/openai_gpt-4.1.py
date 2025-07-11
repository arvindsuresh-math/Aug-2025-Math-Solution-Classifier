def solve():
    """Index: 1466.
    Returns: the total number of times 2 dogs will have barked after 10 minutes.
    """
    # L1
    num_dogs = 2 # 2 dogs
    barks_per_dog_per_minute = 30 # barks 30 times per minute
    barks_per_minute = num_dogs * barks_per_dog_per_minute

    # L2
    minutes = 10 # after 10 minutes
    total_barks = barks_per_minute * minutes

    # FA
    answer = total_barks
    return answer