def solve():
    """Index: 5432.
    Returns: the average age of the 1st and 5th fastest dogs.
    """
    # L1
    age_1st_dog = 10 # 1st fastest dog is 10 years old
    age_difference_2nd_dog = 2 # 2 years younger than the first fastest dog
    age_2nd_dog = age_1st_dog - age_difference_2nd_dog

    # L2
    age_increase_3rd_dog = 4 # 4 years older than the 2nd fastest dog
    age_3rd_dog = age_2nd_dog + age_increase_3rd_dog

    # L3
    half_factor = 2 # half the age
    age_4th_dog = (1 / half_factor) * age_3rd_dog

    # L4
    age_increase_5th_dog = 20 # 20 years older than the 4th fastest dog
    age_5th_dog = age_4th_dog + age_increase_5th_dog

    # L5
    total_age_1st_5th_dogs = age_5th_dog + age_1st_dog

    # L6
    number_of_dogs_for_average = 2 # WK
    average_age = total_age_1st_5th_dogs / number_of_dogs_for_average

    # FA
    answer = average_age
    return answer