def solve():
    """Index: 3040.
    Returns: how many years younger Tim is than Jenny.
    """
    # L1
    tim_age = 5 # Tim is 5 years old
    rommel_multiplier = 3 # thrice as old as he is
    rommel_age = tim_age * rommel_multiplier

    # L2
    jenny_age_diff_rommel = 2 # 2 years older than Rommel
    jenny_age = rommel_age + jenny_age_diff_rommel

    # L3
    age_difference = jenny_age - tim_age

    # FA
    answer = age_difference
    return answer