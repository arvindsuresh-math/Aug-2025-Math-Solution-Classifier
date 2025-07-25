def solve():
    """Index: 6715.
    Returns: the height of the highest throw.
    """
    # L1
    christine_first_throw = 20 # Christine throws it 20 feet high
    christine_second_throw_increase = 10 # ten feet higher than her first throw
    christine_second_throw = christine_first_throw + christine_second_throw_increase

    # L2
    christine_third_throw_increase = 4 # 4 feet higher than her 2nd throw
    christine_third_throw = christine_second_throw + christine_third_throw_increase

    # L3
    janice_first_throw_decrease = 4 # 4 feet lower than Christine's
    janice_first_throw = christine_first_throw - janice_first_throw_decrease

    # L4
    janice_second_throw_multiplier = 2 # twice as high as her first throw
    janice_second_throw = janice_first_throw * janice_second_throw_multiplier

    # L5
    janice_third_throw_increase = 17 # 17 feet higher than Christine's first throw
    janice_third_throw = christine_first_throw + janice_third_throw_increase

    # L6
    highest_throw = max(christine_first_throw, christine_second_throw, christine_third_throw, janice_first_throw, janice_second_throw, janice_third_throw)

    # FA
    answer = highest_throw
    return answer