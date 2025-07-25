def solve():
    """Index: 3991.
    Returns: the total number of soccer balls the public official would donate.
    """
    # L1
    elementary_classes_per_school = 4 # 4 elementary school classes
    middle_classes_per_school = 5 # 5 middle school classes
    total_classes_per_school = elementary_classes_per_school + middle_classes_per_school

    # L2
    num_schools = 2 # two schools
    total_classes_all_schools = total_classes_per_school * num_schools

    # L3
    soccer_balls_per_class = 5 # 5 new soccer balls per each class
    total_soccer_balls_donated = total_classes_all_schools * soccer_balls_per_class

    # FA
    answer = total_soccer_balls_donated
    return answer