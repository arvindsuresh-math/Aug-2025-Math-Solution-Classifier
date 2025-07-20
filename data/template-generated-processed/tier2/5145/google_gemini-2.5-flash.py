def solve():
    """Index: 5145.
    Returns: the class average on the test.
    """
    # L1
    total_percent = 100 # WK
    boys_percent = 40 # 40% boys
    girls_percent = total_percent - boys_percent

    # L2
    boys_score = 80 # Every boy in class gets an 80% on the math test
    girls_score = 90 # Every girl gets a 90%
    boys_decimal_val = 0.4 # from solution text: .4(80)
    girls_decimal_val = 0.6 # from solution text: .6(90)
    class_average = boys_decimal_val * boys_score + girls_decimal_val * girls_score

    # FA
    answer = class_average
    return answer