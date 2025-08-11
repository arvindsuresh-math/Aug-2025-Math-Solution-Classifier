def solve():
    """Index: 4848.
    Returns: the number of women working at Sarah's company.
    """
    # L1
    total_percent = 100 # WK
    men_with_degree_percent_num = 75 # 75% have a college degree
    men_no_degree_percent_num = total_percent - men_with_degree_percent_num

    # L2
    men_no_degree_count = 8 # 8 do not
    men_no_degree_percent_decimal = 0.25 # WK
    total_men = men_no_degree_count / men_no_degree_percent_decimal

    # L3
    women_percent_num = 60 # 60% of the employees are women
    men_percent_num = total_percent - women_percent_num

    # L4
    men_percent_decimal = 0.4 # WK
    total_employees = total_men / men_percent_decimal

    # L5
    total_women = total_employees - total_men

    # FA
    answer = total_women
    return answer