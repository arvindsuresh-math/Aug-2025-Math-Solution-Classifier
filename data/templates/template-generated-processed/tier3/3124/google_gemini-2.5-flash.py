def solve():
    """Index: 3124.
    Returns: the total number of pieces of clothing Nicole ends up with.
    """
    # L1
    nicole_initial_clothes = 10 # Nicole started with 10 pieces of clothing
    half_divisor = 2 # half as many clothes
    first_sister_clothes = nicole_initial_clothes / half_divisor

    # L2
    more_than_nicole = 2 # 2 more pieces of clothing than Nicole
    second_sister_clothes = nicole_initial_clothes + more_than_nicole

    # L3
    sum_three_youngest = nicole_initial_clothes + first_sister_clothes + second_sister_clothes

    # L4
    average_divisor = 3 # average of what her three younger sisters had
    oldest_sister_clothes = sum_three_youngest / average_divisor

    # L5
    total_nicole_clothes = nicole_initial_clothes + first_sister_clothes + second_sister_clothes + oldest_sister_clothes

    # FA
    answer = total_nicole_clothes
    return answer