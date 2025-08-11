def solve():
    """Index: 650.
    Returns: the number of candies left to be shared with others.
    """
    # L1
    num_siblings = 3 # his 3 siblings
    candies_per_sibling = 10 # 10 candies each
    candies_given_to_siblings = num_siblings * candies_per_sibling

    # L2
    initial_candies = 100 # 100 gummy bear candies
    candies_after_siblings = initial_candies - candies_given_to_siblings

    # L3
    friend_share_divisor = 2 # half of the remaining candies
    candies_given_to_friend = candies_after_siblings / friend_share_divisor

    # L4
    candies_after_friend = candies_after_siblings - candies_given_to_friend

    # L5
    candies_to_eat = 16 # only wants to eat 16 gummy bear candies
    candies_for_sharing = candies_after_friend - candies_to_eat

    # FA
    answer = candies_for_sharing
    return answer