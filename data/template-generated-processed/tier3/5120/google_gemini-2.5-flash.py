def solve():
    """Index: 5120.
    Returns: the total time Marcy spends with her cat.
    """
    # L1
    petting_time = 12 # 12 minutes petting her cat
    combing_divisor = 3 # 1/3 of that time combing it
    combing_time = petting_time / combing_divisor

    # L2
    total_time = combing_time + petting_time

    # FA
    answer = total_time
    return answer