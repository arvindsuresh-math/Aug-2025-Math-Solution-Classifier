def solve(
    candy_per_house_anna: int = 14,  # Anna gets 14 pieces of candy per house
    houses_anna: int = 60,  # first subdivision has 60 houses
    candy_per_house_billy: int = 11,  # Billy gets 11 pieces of candy per house
    houses_billy: int = 75  # second subdivision has 75 houses
):
    """Index: 39.
    Returns: the number of more pieces of candy Anna gets compared to Billy.
    """

    #: L1
    total_candy_anna = candy_per_house_anna * houses_anna

    #: L2
    total_candy_billy = candy_per_house_billy * houses_billy

    #: L3
    difference_candy = total_candy_anna - total_candy_billy

    #: FA
    answer = difference_candy
    return answer