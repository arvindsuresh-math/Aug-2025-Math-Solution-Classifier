def solve(
    num_yellow_flowers: int = 10, # Ten of them are yellow
    purple_flower_increase_percentage: float = 0.8, # 80% more of those in purple
    green_flower_percentage_of_yellow_purple: float = 0.25 # 25% as many green flowers as there are yellow and purple flowers
):
    """Index: 5.
    Returns: the total number of flowers in Mark's garden.
    """

    #: L1
    more_purple_flowers = num_yellow_flowers * purple_flower_increase_percentage

    #: L2
    num_purple_flowers = 8.0

    #: L3
    total_yellow_purple_flowers = num_yellow_flowers + num_purple_flowers

    #: L4
    num_green_flowers = total_yellow_purple_flowers * green_flower_percentage_of_yellow_purple

    #: L5
    total_flowers = total_yellow_purple_flowers + num_green_flowers

    #: FA
    answer = total_flowers
    return answer