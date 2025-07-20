def solve():
    """Index: 6941.
    Returns: the number of female adults present.
    """
    # L1
    children_present = 80 # number of children present was 80
    male_adults = 60 # 60 male adults
    total_male_adults_children = children_present + male_adults

    # L2
    total_people = 200 # total number of people in the church was 200
    female_adults = total_people - total_male_adults_children

    # FA
    answer = female_adults
    return answer