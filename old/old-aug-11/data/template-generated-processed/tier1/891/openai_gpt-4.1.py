def solve():
    """Index: 891.
    Returns: how many years older Lavinia's son is than Lavinia's daughter.
    """
    # L1
    katies_daughter_age = 12 # Katie’s daughter is 12 years old
    lavinias_daughter_younger = 10 # Lavinia’s daughter is 10 years younger
    lavinias_daughter_age = katies_daughter_age - lavinias_daughter_younger

    # L2
    lavinias_son_times = 2 # Lavinia’s son is 2 times the age
    lavinias_son_age = katies_daughter_age * lavinias_son_times

    # L3
    age_difference = lavinias_son_age - lavinias_daughter_age

    # FA
    answer = age_difference
    return answer