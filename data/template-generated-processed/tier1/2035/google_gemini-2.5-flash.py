def solve():
    """Index: 2035.
    Returns: the total number of kittens at the shelter.
    """
    # L1
    num_puppies = 32 # 32 puppies at the shelter
    multiplier_for_two_times = 2 # two times the number of puppies
    two_times_puppies = num_puppies * multiplier_for_two_times

    # L2
    more_kittens = 14 # 14 more kittens
    total_kittens = two_times_puppies + more_kittens

    # FA
    answer = total_kittens
    return answer