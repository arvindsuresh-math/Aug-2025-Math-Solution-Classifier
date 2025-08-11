def solve():
    """Index: 3540.
    Returns: the difference in home runs scored between the Chicago Cubs and the Cardinals.
    """
    # L1
    cubs_hr_third_inning = 2 # 2 home runs in the third inning
    cubs_hr_fifth_inning = 1 # 1 home run in the fifth inning
    cubs_hr_eighth_inning = 2 # 2 more home runs in the eighth inning
    cubs_total_hr = cubs_hr_third_inning + cubs_hr_fifth_inning + cubs_hr_eighth_inning

    # L2
    cardinals_hr_second_inning = 1 # 1 home run in the second inning
    cardinals_hr_fifth_inning = 1 # 1 home run in the fifth inning
    cardinals_total_hr = cardinals_hr_second_inning + cardinals_hr_fifth_inning

    # L3
    hr_difference = cubs_total_hr - cardinals_total_hr

    # FA
    answer = hr_difference
    return answer