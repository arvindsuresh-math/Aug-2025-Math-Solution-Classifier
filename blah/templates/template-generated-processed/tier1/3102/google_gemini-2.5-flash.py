def solve():
    """Index: 3102.
    Returns: the total number of animal crackers eaten by the students.
    """
    # L1
    total_students = 20 # 20 students in her class
    students_did_not_eat = 2 # 2 students did not eat their animal crackers
    students_who_ate = total_students - students_did_not_eat

    # L2
    crackers_per_pack = 10 # Each pack of animal crackers contained 10 animal crackers
    total_crackers_eaten = students_who_ate * crackers_per_pack

    # FA
    answer = total_crackers_eaten
    return answer