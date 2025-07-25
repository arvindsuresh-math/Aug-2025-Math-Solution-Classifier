def solve():
    """Index: 1041.
    Returns: the number of vaccinated children.
    """
    # L1
    adult_percent = 80 # 80% of the people were adults
    total_percent = 100 # WK
    children_percent = total_percent - adult_percent

    # L3
    children_percent_decimal = 0.2 # WK
    total_vaccinated_people = 650 # 650 people
    num_children_vaccinated = children_percent_decimal * total_vaccinated_people

    # FA
    answer = num_children_vaccinated
    return answer