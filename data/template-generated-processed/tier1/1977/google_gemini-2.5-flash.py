def solve():
    """Index: 1977.
    Returns: the total dollars Charles will earn.
    """
    # L1
    housesitting_rate = 15 # $15 per hour when he housesits
    housesitting_hours = 10 # housesits for 10 hours
    housesitting_earnings = housesitting_rate * housesitting_hours

    # L2
    dog_walking_rate = 22 # $22 per hour when he walks a dog
    num_dogs_walked = 3 # walks 3 dogs
    dog_walking_earnings = dog_walking_rate * num_dogs_walked

    # L3
    total_earned = housesitting_earnings + dog_walking_earnings

    # FA
    answer = total_earned
    return answer