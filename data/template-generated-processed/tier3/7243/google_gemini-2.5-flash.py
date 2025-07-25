def solve():
    """Index: 7243.
    Returns: the total number of students at the restaurant.
    """
    # L1
    burger_students = 30 # number of students who ordered burgers was 30
    twice_factor = 2 # twice the number of students
    hot_dog_students = burger_students / twice_factor

    # L2
    total_students = hot_dog_students + burger_students

    # FA
    answer = total_students
    return answer