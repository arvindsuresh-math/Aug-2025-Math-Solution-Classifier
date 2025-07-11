def solve():
    """Index: 2031.
    Returns: the number of questions Martin answered correctly.
    """
    # L1
    campbell_correct = 35 # Campbell answered 35 questions correctly
    kelsey_more_than_campbell = 8 # Kelsey answered eight more questions correctly than Campbell
    kelsey_correct = campbell_correct + kelsey_more_than_campbell

    # L2
    martin_fewer_than_kelsey = 3 # Martin answered three fewer questions correctly than Kelsey
    martin_correct = kelsey_correct - martin_fewer_than_kelsey

    # FA
    answer = martin_correct
    return answer