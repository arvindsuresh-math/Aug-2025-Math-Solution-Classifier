def solve():
    """Index: 2125.
    Returns: the age difference in dog years.
    """
    # L1
    dog_current_human_years = 3 # 3-year-old dog
    dog_age_factor = 7 # a dog ages 7 years
    dog_age_in_dog_years = dog_current_human_years * dog_age_factor

    # L2
    max_age_human_years = 3 # When Max is 3
    age_difference = dog_age_in_dog_years - max_age_human_years

    # FA
    answer = age_difference
    return answer