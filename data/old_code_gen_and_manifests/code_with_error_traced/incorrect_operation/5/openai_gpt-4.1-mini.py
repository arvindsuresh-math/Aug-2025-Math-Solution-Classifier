def solve(
    yellow_flowers: int = 10,  # Ten of them are yellow
    purple_more_percent: float = 0.8,  # 80% more of those in purple
    green_fraction: float = 0.25  # 25% as many green flowers as yellow and purple flowers
):
    """Index: 5.
    Returns: the total number of flowers in Mark's garden.
    """

    #: L1
    purple_more = purple_more_percent - yellow_flowers # eval: -9.2 = 0.8 - 10

    #: L2
    purple_flowers = yellow_flowers + purple_more # eval: 0.8000000000000007 = 10 + -9.2

    #: L3
    yellow_purple_sum = yellow_flowers + purple_flowers # eval: 10.8 = 10 + 0.8000000000000007

    #: L4
    green_flowers = green_fraction * yellow_purple_sum # eval: 2.7 = 0.25 * 10.8

    #: L5
    total_flowers = yellow_purple_sum + green_flowers # eval: 13.5 = 10.8 + 2.7

    #: FA
    answer = total_flowers
    return answer # eval: return 13.5
