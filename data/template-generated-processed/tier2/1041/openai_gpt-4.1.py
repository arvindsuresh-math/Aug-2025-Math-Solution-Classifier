def solve():
    """Index: 1041.
    Returns: the number of vaccinated people who were children.
    """
    # L1
    total_percent = 100 # WK
    percent_adults = 80 # 80% of the people were adults
    percent_children = total_percent - percent_adults

    # L2
    total_vaccinated = 650 # 650 people
    # percent_children already defined

    # L3
    percent_children_decimal = 0.2 # 20% = 0.2
    num_children = percent_children_decimal * total_vaccinated

    # FA
    answer = num_children
    return answer