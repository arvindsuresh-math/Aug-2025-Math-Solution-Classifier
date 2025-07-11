def solve():
    """Index: 1977.
    Returns: the total dollars Charles will earn from housesitting and dog walking.
    """
    # L1
    housesit_rate = 15 # $15 per hour when he housesits
    housesit_hours = 10 # housesits for 10 hours
    housesit_earnings = housesit_rate * housesit_hours

    # L2
    dogwalk_rate = 22 # $22 per hour when he walks a dog
    num_dogs = 3 # walks 3 dogs
    dogwalk_earnings = dogwalk_rate * num_dogs

    # L3
    total_earned = housesit_earnings + dogwalk_earnings

    # FA
    answer = total_earned
    return answer