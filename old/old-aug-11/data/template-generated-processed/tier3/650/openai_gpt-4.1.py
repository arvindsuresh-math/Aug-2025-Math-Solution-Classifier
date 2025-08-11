def solve():
    """Index: 650.
    Returns: the number of candies left to be shared with others.
    """
    # L1
    num_siblings = 3 # his 3 siblings
    candies_per_sibling = 10 # 10 candies each
    candies_given_to_siblings = num_siblings * candies_per_sibling

    # L2
    initial_candies = 100 # Josh had 100 gummy bear candies
    candies_after_siblings = initial_candies - candies_given_to_siblings

    # L3
    best_friend_divisor = 2 # gave half of the remaining candies
    candies_given_to_best_friend = candies_after_siblings / best_friend_divisor

    # L4
    candies_after_best_friend = candies_after_siblings - candies_given_to_best_friend

    # L5
    candies_josh_eats = 16 # he only wants to eat 16 gummy bear candies
    candies_left_to_share = candies_after_best_friend - candies_josh_eats

    # FA
    answer = candies_left_to_share
    return answer