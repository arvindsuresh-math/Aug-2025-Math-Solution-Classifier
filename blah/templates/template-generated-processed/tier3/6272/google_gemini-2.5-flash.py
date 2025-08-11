def solve():
    """Index: 6272.
    Returns: the probability of picking a blue candy as a percentage.
    """
    # L1
    green_candies = 5 # 5 green candies
    blue_candies = 3 # 3 blue candies
    red_candies = 4 # 4 red candies
    total_candies = green_candies + blue_candies + red_candies

    # L2
    percentage_multiplier = 100 # WK
    probability_blue_percentage = (blue_candies / total_candies) * percentage_multiplier

    # FA
    answer = probability_blue_percentage
    return answer