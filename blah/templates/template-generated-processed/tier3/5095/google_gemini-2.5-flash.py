def solve():
    """Index: 5095.
    Returns: the total number of presents David found.
    """
    # L1
    christmas_presents = 60 # a total of 60 Christmas presents
    ratio_christmas_to_birthday = 2 # twice as many as the number of birthday presents
    birthday_presents = christmas_presents / ratio_christmas_to_birthday

    # L2
    total_presents = birthday_presents + christmas_presents

    # FA
    answer = total_presents
    return answer