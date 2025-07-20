def solve():
    """Index: 7406.
    Returns: the total number of more boys competing than girls.
    """
    # L1
    girls_4th_class1 = 12 # The first 4th grade class had 12 girls
    girls_4th_class2 = 15 # The second 4th grade class had 15 girls
    girls_5th_class1 = 9 # The first 5th grade class had 9 girls
    girls_5th_class2 = 10 # the second 5th grade class had 10 girls
    total_girls = girls_4th_class1 + girls_4th_class2 + girls_5th_class1 + girls_5th_class2

    # L2
    boys_4th_class1 = 13 # The first 4th grade class had 13 boys
    boys_4th_class2 = 11 # The second 4th grade class had 11 boys
    boys_5th_class1 = 13 # The first 5th grade class had 13 boys
    boys_5th_class2 = 11 # the second 5th grade class had 11 boys
    total_boys = boys_4th_class1 + boys_4th_class2 + boys_5th_class1 + boys_5th_class2

    # L3
    more_boys_than_girls = total_boys - total_girls

    # FA
    answer = more_boys_than_girls
    return answer