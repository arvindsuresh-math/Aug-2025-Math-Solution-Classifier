def solve():
    """Index: 1995.
    Returns: the number of photographs needed to reach the target.
    """
    # L1
    initial_photographs = 100 # 100 photographs of our project
    fewer_percentage_numerator = 20 # 20% fewer photographs
    percentage_denominator = 100 # WK
    fewer_photographs = (fewer_percentage_numerator / percentage_denominator) * initial_photographs

    # L2
    today_photographs = initial_photographs - fewer_photographs

    # L3
    total_photographs_taken = today_photographs + initial_photographs

    # L4
    target_photographs = 300 # 300 photographs of the project
    photographs_needed = target_photographs - total_photographs_taken

    # FA
    answer = photographs_needed
    return answer