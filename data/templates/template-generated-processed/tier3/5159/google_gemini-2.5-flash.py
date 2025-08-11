def solve():
    """Index: 5159.
    Returns: the total number of students in Peter's class including him.
    """
    # L1
    hands_excluding_peter = 20 # 20 hands in Peter’s class, not including his
    peter_hands = 2 # Assume every student in the class has 2 arms and 2 hands
    total_hands = hands_excluding_peter + peter_hands

    # L2
    hands_per_student = 2 # Assume every student in the class has 2 arms and 2 hands
    total_students = total_hands / hands_per_student

    # FA
    answer = total_students
    return answer