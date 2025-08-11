def solve():
    """Index: 804.
    Returns: the number of panda babies born.
    """
    # L1
    num_pandas = 16 # 16 pandas
    pandas_per_couple = 2 # WK
    num_panda_couples = num_pandas / pandas_per_couple

    # L2
    pregnant_percent_num = 25 # 25% of the panda couples get pregnant
    percent_factor = 0.01 # WK
    babies_per_couple = 1 # If they each have one baby
    num_panda_babies = num_panda_couples * pregnant_percent_num * percent_factor * babies_per_couple

    # FA
    answer = num_panda_babies
    return answer