def solve():
    """Index: 2035.
    Returns: the number of kittens at the animal shelter.
    """
    # L1
    puppies = 32 # 32 puppies at the shelter
    multiplier = 2 # two times the number of puppies
    twice_puppies = puppies * multiplier

    # L2
    more_kittens = 14 # 14 more kittens than two times the number of puppies
    kittens = twice_puppies + more_kittens

    # FA
    answer = kittens
    return answer