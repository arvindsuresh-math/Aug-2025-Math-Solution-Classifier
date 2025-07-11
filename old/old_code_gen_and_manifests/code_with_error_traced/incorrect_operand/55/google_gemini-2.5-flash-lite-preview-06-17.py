def solve(
    num_roses: int = 25, # There are 25 roses
    num_tulips: int = 40, # There are 40 tulips
    num_daisies: int = 35 # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """

    #: L1
    total_flowers = num_roses + num_tulips + num_tulips # eval: 105 = 25 + 40 + 40

    #: L2
    flowers_not_roses = num_tulips + num_daisies # eval: 75 = 40 + 35

    #: L3
    percentage_not_roses = (flowers_not_roses / total_flowers) * 100 # eval: 71.42857142857143 = (75 / 105) * 100

    #: FA
    answer = percentage_not_roses
    return answer # eval: return 71.42857142857143
