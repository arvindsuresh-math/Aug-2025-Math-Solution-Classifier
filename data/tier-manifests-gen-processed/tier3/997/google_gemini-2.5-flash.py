def solve():
    """Index: 997.
    Returns: the number of fish each person will be given to eat.
    """
    # L1
    dog_eyes_eaten = 2 # two of the eyes to his dog
    oomyapeck_eyes_eaten = 22 # eats 22 eyes in a day
    total_eyes = dog_eyes_eaten + oomyapeck_eyes_eaten

    # L2
    eyes_per_fish = 2 # 2 eyes per fish
    total_fish = total_eyes / eyes_per_fish

    # L3
    number_of_people = 3 # the three of them
    fish_per_person = total_fish / number_of_people

    # FA
    answer = fish_per_person
    return answer