def solve():
    """Index: 1816.
    Returns: the total number of legs' worth of organisms traveling together for the walk.
    """
    # L1
    num_humans = 2 # Johnny and his son
    human_legs = 2 # humans walk on two legs
    human_legs_total = num_humans * human_legs

    # L2
    num_dogs = 2 # two dogs
    dog_legs = 4 # dogs walk on 4 legs
    dog_legs_total = num_dogs * dog_legs

    # L3
    total_legs = human_legs_total + dog_legs_total

    # FA
    answer = total_legs
    return answer