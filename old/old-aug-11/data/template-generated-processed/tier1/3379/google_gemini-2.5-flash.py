def solve():
    """Index: 3379.
    Returns: the number of questions Cherry answered correctly.
    """
    # L1
    nicole_correct = 22 # Nicole answered 22 correctly
    nicole_fewer_than_kim = 3 # 3 fewer questions correctly than Kim
    kim_correct = nicole_correct + nicole_fewer_than_kim

    # L2
    kim_more_than_cherry = 8 # 8 more questions correctly than Cherry
    cherry_correct = kim_correct - kim_more_than_cherry

    # FA
    answer = cherry_correct
    return answer