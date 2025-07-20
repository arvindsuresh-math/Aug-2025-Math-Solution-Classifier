def solve():
    """Index: 3863.
    Returns: the total number of minutes it takes to groom the dogs and cats.
    """
    # L1
    time_per_dog_hours = 2.5 # 2.5 hours to groom a dog
    num_dogs = 5 # 5 dogs
    total_dog_grooming_hours = time_per_dog_hours * num_dogs

    # L2
    time_per_cat_hours = 0.5 # 0.5 hours to groom a cat
    num_cats = 3 # 3 cats
    total_cat_grooming_hours = time_per_cat_hours * num_cats

    # L3
    total_grooming_hours = total_dog_grooming_hours + total_cat_grooming_hours

    # L4
    minutes_per_hour = 60 # WK
    total_grooming_minutes = total_grooming_hours * minutes_per_hour

    # FA
    answer = total_grooming_minutes
    return answer