def solve(
    num_roses: int = 25, # There are 25 roses in a garden
    num_tulips: int = 40, # There are 40 tulips
    num_daisies: int = 35 # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    #: L1
    total_flowers = num_roses + num_tulips + num_daisies

    #: L2
    flowers_not_roses = num_tulips + num_daisies

    #: L3
    percentage_not_roses = (flowers_not_roses / total_flowers) * 100

    answer = percentage_not_roses # FINAL ANSWER
    return answer