def solve():
    """Index: 4097.
    Returns: the number of singers at the party.
    """
    # L1
    more_poets_than_treehuggers = 50 # 50 more poets than treehuggers
    num_treehuggers = 120 # number of tree huggers is 120
    num_poets = num_treehuggers + more_poets_than_treehuggers

    # L2
    total_poets_treehuggers = num_poets + num_treehuggers

    # L3
    total_students = 400 # 400 students
    num_singers = total_students - total_poets_treehuggers

    # FA
    answer = num_singers
    return answer