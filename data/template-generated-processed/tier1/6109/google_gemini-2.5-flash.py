def solve():
    """Index: 6109.
    Returns: the number of candies Susan ate during the week.
    """
    # L1
    candies_tuesday = 3 # bought 3 on Tuesday
    candies_thursday = 5 # 5 on Thursday
    candies_friday = 2 # 2 on Friday
    total_bought = candies_tuesday + candies_thursday + candies_friday

    # L2
    candies_left = 4 # only 4 of them left
    candies_eaten = total_bought - candies_left

    # FA
    answer = candies_eaten
    return answer