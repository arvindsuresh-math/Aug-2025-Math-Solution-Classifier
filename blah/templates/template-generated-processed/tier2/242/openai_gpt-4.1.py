def solve():
    """Index: 242.
    Returns: the total number of cookies Ann keeps.
    """
    # L1
    oatmeal_baked = 3 # three dozen oatmeal raisin cookies
    oatmeal_given = 2 # gives away two dozen oatmeal raisin cookies
    oatmeal_left = oatmeal_baked - oatmeal_given

    # L2
    sugar_baked = 2 # two dozen sugar cookies
    sugar_given = 1.5 # 1.5 dozen sugar cookies
    sugar_left = sugar_baked - sugar_given

    # L3
    chocolate_baked = 4 # four dozen chocolate chip cookies
    chocolate_given = 2.5 # 2.5 dozen chocolate chip cookies
    chocolate_left = chocolate_baked - chocolate_given

    # L4
    total_dozens_left = oatmeal_left + sugar_left + chocolate_left

    # L5
    dozen = 12 # WK
    answer = total_dozens_left * dozen
    return answer