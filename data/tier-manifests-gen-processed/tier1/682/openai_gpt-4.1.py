def solve():
    """Index: 682.
    Returns: the amount Roe should save in December to reach $150 total savings for the year.
    """
    # L1
    months_jan_jul = 7 # 7 months from January to July
    savings_per_month_jan_jul = 10 # $10 per month from January to July
    savings_jan_jul = months_jan_jul * savings_per_month_jan_jul

    # L2
    months_aug_nov = 4 # 4 months from August to November
    savings_per_month_aug_nov = 15 # $15 per month from August to November
    savings_aug_nov = months_aug_nov * savings_per_month_aug_nov

    # L3
    savings_jan_nov = savings_jan_jul + savings_aug_nov

    # L4
    total_goal = 150 # total savings of $150 in the year
    savings_december = total_goal - savings_jan_nov

    # FA
    answer = savings_december
    return answer