def solve():
    """Index: 3044.
    Returns: the number of packages of noodles Tom needs to buy.
    """
    # L1
    beef_pounds = 10 # He has 10 pounds of beef
    noodles_multiplier = 2 # It takes twice as many noodles as beef
    total_noodles_needed = beef_pounds * noodles_multiplier

    # L2
    noodles_already_have = 4 # He already has 4 pounds of lasagna noodles
    noodles_to_buy = total_noodles_needed - noodles_already_have

    # L3
    pounds_per_package = 2 # the noodles come in 2-pound packages
    packages_to_buy = noodles_to_buy / pounds_per_package

    # FA
    answer = packages_to_buy
    return answer