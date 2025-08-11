def solve():
    """Index: 5737.
    Returns: the number of candies each friend will receive.
    """
    # L1
    initial_candies = 20 # Paula has 20 candies
    additional_candies = 4 # buy four additional candies
    total_candies = initial_candies + additional_candies

    # L2
    num_friends = 6 # her six friends
    candies_per_friend = total_candies / num_friends

    # FA
    answer = candies_per_friend
    return answer