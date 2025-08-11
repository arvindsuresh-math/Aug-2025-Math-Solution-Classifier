def solve():
    """Index: 1563.
    Returns: the total number of cows Aaron, Matthews, and Marovich have altogether.
    """
    # L1
    matthews_cows = 60 # Matthews has 60 cows
    aaron_multiplier = 4 # Aaron has four times as many cows as Matthews
    aaron_cows = aaron_multiplier * matthews_cows

    # L2
    aaron_matthews_total = aaron_cows + matthews_cows

    # L3
    marovich_fewer = 30 # 30 more cows than Marovich => Marovich has 30 fewer
    marovich_cows = aaron_matthews_total - marovich_fewer

    # L4
    total_cows = marovich_cows + aaron_matthews_total

    # FA
    answer = total_cows
    return answer