def solve():
    """Index: 6587.
    Returns: the total number of students who own dogs.
    """
    # L1
    total_students = 100 # 100 students
    half_divisor = 2 # Half of the students
    num_girls = total_students / half_divisor

    # L2
    num_boys = total_students - num_girls

    # L3
    girls_dog_percent_num = 20 # 20% of the girls
    girls_dog_percent_decimal = 0.20 # 20% of the girls
    percent_factor = 0.01 # WK
    girls_with_dogs = girls_dog_percent_num * percent_factor * num_girls

    # L4
    boys_dog_percent_decimal = 0.10 # 10% of the boys
    boys_with_dogs = boys_dog_percent_decimal * num_boys

    # L5
    total_dogs = girls_with_dogs + boys_with_dogs

    # FA
    answer = total_dogs
    return answer