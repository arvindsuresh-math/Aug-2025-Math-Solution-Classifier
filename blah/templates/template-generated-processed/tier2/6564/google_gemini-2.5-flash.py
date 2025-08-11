def solve():
    """Index: 6564.
    Returns: the total number of people polled.
    """
    # L1
    total_percent = 100 # WK
    women_in_favor_percent = 35 # 35% of women are in favor
    women_opposed_percent = total_percent - women_in_favor_percent

    # L2
    women_opposed_count = 39 # 39 women in her poll opposed this idea
    women_opposed_decimal = 0.65 # from solution text: .65
    total_women_polled = women_opposed_count / women_opposed_decimal

    # L3
    women_percentage_of_total = 0.5 # 50% women
    total_people_polled = total_women_polled / women_percentage_of_total

    # FA
    answer = total_people_polled
    return answer