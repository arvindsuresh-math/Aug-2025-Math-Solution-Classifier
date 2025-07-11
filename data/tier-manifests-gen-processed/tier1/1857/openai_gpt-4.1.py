def solve():
    """Index: 1857.
    Returns: the total number of people who attended the family reunion.
    """
    # L1
    male_adults = 100 # 100 male adults
    female_more_than_male = 50 # 50 more female adults than male adults
    female_adults = male_adults + female_more_than_male

    # L2
    total_adults = female_adults + male_adults

    # L3
    children_multiplier = 2 # children were twice the total number of adults
    children = children_multiplier * total_adults

    # L4
    total_people = children + total_adults

    # FA
    answer = total_people
    return answer