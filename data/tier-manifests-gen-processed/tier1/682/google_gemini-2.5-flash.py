def solve():
    """Index: 682.
    Returns: the amount Roe should save in December.
    """
    # L1
    savings_jan_jul_per_month = 10 # saved $10 per month from January to July
    months_jan_jul = 7 # 7 months from January to July
    savings_jan_jul_total = savings_jan_jul_per_month * months_jan_jul

    # L2
    savings_aug_nov_per_month = 15 # saved $15 per month from August to November
    months_aug_nov = 4 # 4 months from August to November
    savings_aug_nov_total = savings_aug_nov_per_month * months_aug_nov

    # L3
    savings_jan_nov_total = savings_jan_jul_total + savings_aug_nov_total

    # L4
    target_total_savings = 150 # total savings of $150 in the year
    savings_december = target_total_savings - savings_jan_nov_total

    # FA
    answer = savings_december
    return answer