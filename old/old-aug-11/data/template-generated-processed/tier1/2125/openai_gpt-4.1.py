def solve():
    """Index: 2125.
    Returns: how much older, in dog years, Max's 3-year-old dog will be than Max when Max is 3.
    """
    # L1
    dog_age_human_years = 3 # 3-year-old dog
    dog_to_human_ratio = 7 # a dog ages 7 years to one human year
    dog_age_dog_years = dog_age_human_years * dog_to_human_ratio

    # L2
    max_age = 3 # Max is 3
    age_difference = dog_age_dog_years - max_age

    # FA
    answer = age_difference
    return answer