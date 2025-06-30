def solve(
    yellow_flowers: int = 10,  # Ten of them are yellow
    purple_more_percent: float = 0.8,  # 80% more of those in purple
    green_fraction: float = 0.25  # 25% as many green flowers as yellow and purple flowers
):
    """Index: 5.
    Returns: the total number of flowers in Mark's garden.
    """

    #: L1
    purple_more = purple_more_percent * yellow_flowers

    #: L2
    purple_flowers = yellow_flowers + purple_more

    #: L3
    yellow_purple_sum = yellow_flowers + purple_flowers

    #: L4
    green_flowers = -3.0

    #: L5
    total_flowers = yellow_purple_sum + green_flowers

    #: FA
    answer = total_flowers
    return answer