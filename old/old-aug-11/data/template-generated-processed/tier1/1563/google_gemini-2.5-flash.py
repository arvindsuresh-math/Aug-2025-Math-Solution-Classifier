def solve():
    """Index: 1563.
    Returns: the total number of cows the three (Aaron, Matthews, and Marovich) have altogether.
    """
    # L1
    matthews_cows = 60 # Matthews has 60 cows
    aaron_multiplier = 4 # four times as many cows as does Matthews
    aaron_cows = aaron_multiplier * matthews_cows

    # L2
    aaron_matthews_total_cows = aaron_cows + matthews_cows

    # L3
    marovich_fewer_than_combined = 30 # 30 more cows than Marovich (implies Marovich has 30 fewer)
    marovich_cows = aaron_matthews_total_cows - marovich_fewer_than_combined

    # L4
    total_cows_three = marovich_cows + aaron_matthews_total_cows

    # FA
    answer = total_cows_three
    return answer