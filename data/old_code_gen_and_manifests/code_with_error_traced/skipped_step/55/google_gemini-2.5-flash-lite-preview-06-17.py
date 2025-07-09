def solve(
    num_roses: int = 25, # There are 25 roses
    num_tulips: int = 40, # There are 40 tulips
    num_daisies: int = 35 # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """

    #: L1
    total_flowers = num_roses + num_tulips + num_daisies # eval: 100 = 25 + 40 + 35

    #: L2

    #: L3
    percentage_not_roses = (num_daisies / total_flowers) * 100 # eval: 35.0 = (35 / 100) * 100

    #: FA
    answer = percentage_not_roses
    return answer # eval: return 35.0
