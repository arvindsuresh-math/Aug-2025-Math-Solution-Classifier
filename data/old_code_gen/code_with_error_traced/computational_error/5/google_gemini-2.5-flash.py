def solve(
        num_yellow_flowers: int = 10, # Ten of them are yellow
        purple_increase_percentage: int = 80, # 80% more of those in purple
        green_percentage_of_others: int = 25 # only 25% as many green flowers
    ):
    """Index: 5.
    Returns: the total number of flowers Mark has in his garden.
    """

    #: L1
    more_purple_flowers = (purple_increase_percentage / 100) * num_yellow_flowers # eval: 8.0 = (80 / 100) * 10

    #: L2
    num_purple_flowers = num_yellow_flowers + more_purple_flowers # eval: 18.0 = 10 + 8.0

    #: L3
    total_yellow_purple_flowers = 38.0 # eval: 38.0 = 38.0

    #: L4
    num_green_flowers = (green_percentage_of_others / 100) * total_yellow_purple_flowers # eval: 9.5 = (25 / 100) * 38.0

    #: L5
    total_flowers = total_yellow_purple_flowers + num_green_flowers # eval: 47.5 = 38.0 + 9.5

    #: FA
    answer = total_flowers
    return answer # eval: return 47.5
