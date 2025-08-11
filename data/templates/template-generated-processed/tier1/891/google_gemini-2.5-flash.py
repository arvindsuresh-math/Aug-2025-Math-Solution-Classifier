def solve():
    """Index: 891.
    Returns: how many years older Lavinia's son is than Lavinia's daughter.
    """
    # L1
    katies_daughter_age = 12 # Katie’s daughter is 12 years old
    lavinias_daughter_younger_by = 10 # 10 years younger than Katie’s daughter
    lavinias_daughter_age = katies_daughter_age - lavinias_daughter_younger_by

    # L2
    lavinias_son_times_katies_daughter = 2 # 2 times the age of Katie’s daughter
    lavinias_son_age = katies_daughter_age * lavinias_son_times_katies_daughter

    # L3
    age_difference = lavinias_son_age - lavinias_daughter_age

    # FA
    answer = age_difference
    return answer