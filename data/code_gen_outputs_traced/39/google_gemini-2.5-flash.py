def solve(
        candy_per_house_anna: int = 14, # 14 pieces of candy per house
        candy_per_house_billy: int = 11, # 11 pieces of candy per house
        houses_subdivision_anna: int = 60, # the first subdivision has 60 houses
        houses_subdivision_billy: int = 75 # the second subdivision has 75 houses
    ):
    """Index: 39.
    Returns: the number of additional pieces of candy Anna gets compared to Billy.
    """

    #: L1
    total_candy_anna = candy_per_house_anna * houses_subdivision_anna # eval: 840 = 14 * 60

    #: L2
    total_candy_billy = candy_per_house_billy * houses_subdivision_billy # eval: 825 = 11 * 75

    #: L3
    difference_in_candy = total_candy_anna - total_candy_billy # eval: 15 = 840 - 825

    #: FA
    answer = difference_in_candy # eval: 15 = 15
    return answer # eval: return 15
