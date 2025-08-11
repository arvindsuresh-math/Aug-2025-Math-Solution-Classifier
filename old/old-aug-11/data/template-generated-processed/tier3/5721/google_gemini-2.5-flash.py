def solve():
    """Index: 5721.
    Returns: the number of friends Chenny has.
    """
    # L1
    initial_candies = 10 # 10 pieces of candies
    candies_to_buy = 4 # buy 4 more
    total_candies = initial_candies + candies_to_buy

    # L2
    candies_per_friend = 2 # each of her friends will receive 2 candies
    number_of_friends = total_candies / candies_per_friend

    # FA
    answer = number_of_friends
    return answer