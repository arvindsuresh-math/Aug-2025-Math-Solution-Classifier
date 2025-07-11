def solve(
    num_yellow_flowers: int = 10, # Ten of them are yellow
    percent_more_purple: int = 80, # there are 80% more of those in purple
    percent_green_of_yellow_purple: int = 25 # There are only 25% as many green flowers as there are yellow and purple flowers
):
    """Index: 5.
    Returns: the total number of flowers in the garden.
    """

    #: L1
    more_purple_flowers = (percent_more_purple / 100) * num_yellow_flowers # eval: 8.0 = (80 / 100) * 10

    #: L2
    num_purple_flowers = num_yellow_flowers + percent_more_purple # eval: 90 = 10 + 80

    #: L3
    total_yellow_purple = num_yellow_flowers + num_purple_flowers # eval: 100 = 10 + 90

    #: L4
    num_green_flowers = (percent_green_of_yellow_purple / 100) * total_yellow_purple # eval: 25.0 = (25 / 100) * 100

    #: L5
    total_flowers = total_yellow_purple + num_green_flowers # eval: 125.0 = 100 + 25.0

    #: FA
    answer = total_flowers
    return answer # eval: return 125.0
