def solve(
    yellow_flowers: int = 10,  # Ten of them are yellow
    purple_flower_increase_percentage: float = 0.8,  # 80% more purple flowers
    green_flower_percentage: float = 0.25  # 25% as many green flowers
):
    """Index: 5.
    Returns: the total number of flowers in Mark's garden."""

    #: L1
    additional_purple_flowers = yellow_flowers * purple_flower_increase_percentage # eval: 8.0 = 10 * 0.8

    #: L2
    total_purple_flowers = yellow_flowers + additional_purple_flowers # eval: 18.0 = 10 + 8.0

    #: L3
    yellow_and_purple_flowers = yellow_flowers + total_purple_flowers # eval: 28.0 = 10 + 18.0

    #: L4
    green_flowers = yellow_and_purple_flowers * green_flower_percentage # eval: 7.0 = 28.0 * 0.25

    #: L5
    total_flowers = yellow_and_purple_flowers * green_flowers # eval: 196.0 = 28.0 * 7.0

    #: FA
    answer = total_flowers
    return answer # eval: return 196.0
