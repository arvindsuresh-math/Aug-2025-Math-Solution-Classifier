def solve():
    """Index: 5509.
    Returns: the total number of rainbow nerds in the box.
    """
    # L1
    purple_candies = 10 # 10 purple candies
    more_yellow_than_purple = 4 # 4 more yellow candies
    yellow_candies = purple_candies + more_yellow_than_purple

    # L2
    fewer_green_than_yellow = 2 # 2 fewer green candies than yellow candies
    green_candies = yellow_candies - fewer_green_than_yellow

    # L3
    total_rainbow_nerds = purple_candies + yellow_candies + green_candies

    # FA
    answer = total_rainbow_nerds
    return answer