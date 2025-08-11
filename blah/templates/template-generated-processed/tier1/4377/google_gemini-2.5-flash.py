def solve():
    """Index: 4377.
    Returns: the number of pencils Candy has.
    """
    # L1
    calen_lost_pencils = 10 # lost 10 pencils
    calen_remaining_pencils = 10 # left him with 10 pencils
    calen_original_pencils = calen_remaining_pencils + calen_lost_pencils

    # L2
    calen_more_than_caleb = 5 # 5 more pencils than does Caleb
    caleb_pencils = calen_original_pencils - calen_more_than_caleb

    # L5
    multiplier_for_twice = 2 # twice as many pencils
    caleb_less_than_twice_candy = 3 # 3 less than twice as many pencils
    twice_candy_pencils = caleb_pencils + caleb_less_than_twice_candy

    # L6
    candy_pencils = twice_candy_pencils / multiplier_for_twice

    # FA
    answer = candy_pencils
    return answer