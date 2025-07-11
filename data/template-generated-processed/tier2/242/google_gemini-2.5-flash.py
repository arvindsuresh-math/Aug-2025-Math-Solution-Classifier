def solve():
    """Index: 242.
    Returns: the total number of cookies Ann keeps.
    """
    # L1
    oatmeal_baked_dozens = 3 # three dozen oatmeal raisin cookies
    oatmeal_given_dozens = 2 # two dozen oatmeal raisin cookies
    oatmeal_left_dozens = oatmeal_baked_dozens - oatmeal_given_dozens

    # L2
    sugar_baked_dozens = 2 # two dozen sugar cookies
    sugar_given_dozens = 1.5 # 1.5 dozen sugar cookies
    sugar_left_dozens = sugar_baked_dozens - sugar_given_dozens

    # L3
    chocolate_chip_baked_dozens = 4 # four dozen chocolate chip cookies
    chocolate_chip_given_dozens = 2.5 # 2.5 dozen chocolate chip cookies
    chocolate_chip_left_dozens = chocolate_chip_baked_dozens - chocolate_chip_given_dozens

    # L4
    total_dozens_kept = oatmeal_left_dozens + sugar_left_dozens + chocolate_chip_left_dozens

    # L5
    dozen = 12 # WK
    total_cookies_kept = total_dozens_kept * dozen

    # FA
    answer = total_cookies_kept
    return answer