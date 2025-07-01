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
    num_purple_flowers = num_yellow_flowers + more_purple_flowers # eval: 18.0 = 10 + 8.0

    #: L3
    total_yellow_purple = 27.0 # eval: 27.0 = 27.0

    #: L4
    num_green_flowers = (percent_green_of_yellow_purple / 100) * total_yellow_purple # eval: 6.75 = (25 / 100) * 27.0

    #: L5
    total_flowers = total_yellow_purple + num_green_flowers # eval: 33.75 = 27.0 + 6.75

    #: FA
    answer = total_flowers
    return answer # eval: return 33.75
