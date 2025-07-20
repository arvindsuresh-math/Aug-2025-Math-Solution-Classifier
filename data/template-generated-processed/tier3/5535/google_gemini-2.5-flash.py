def solve():
    """Index: 5535.
    Returns: the average class size.
    """
    # L1
    three_year_olds = 13 # 13 3-year-olds
    four_year_olds = 20 # 20 4-year-olds
    class_one_size = three_year_olds + four_year_olds

    # L2
    five_year_olds = 15 # 15 5-year-olds
    six_year_olds = 22 # 22 six-year-olds
    class_two_size = five_year_olds + six_year_olds

    # L3
    total_kids = class_one_size + class_two_size

    # L4
    number_of_classes = 2 # in one class and ... in another class
    average_class_size = total_kids / number_of_classes

    # FA
    answer = average_class_size
    return answer