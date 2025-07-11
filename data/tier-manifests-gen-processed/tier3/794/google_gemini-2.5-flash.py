def solve():
    """Index: 794.
    Returns: the total number of candies remaining.
    """
    # L1
    red_candies = 40 # 40 red candies
    three_times_red_candies = red_candies * 3

    # L3
    less_than_yellow = 20 # 20 less than three times as many yellow candies
    yellow_candies = three_times_red_candies - less_than_yellow

    # L4
    half_divisor = 2 # half as many blue candies
    blue_candies = yellow_candies / half_divisor

    # L5
    remaining_candies = red_candies + blue_candies

    # FA
    answer = remaining_candies
    return answer