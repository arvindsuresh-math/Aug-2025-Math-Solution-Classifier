def solve():
    """Index: 2347.
    Returns: the total number of candies the three of them have.
    """
    # L1
    james_multiplier = 3 # James has 3 times the number of candies Adam has
    adam_candies = 6 # Adam has 6 candies
    james_candies = james_multiplier * adam_candies

    # L2
    rubert_multiplier = 4 # Rubert has 4 times the number of candies James has
    rubert_candies = rubert_multiplier * james_candies

    # L3
    total_candies = adam_candies + james_candies + rubert_candies

    # FA
    answer = total_candies
    return answer