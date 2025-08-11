def solve():
    """Index: 2683.
    Returns: the number of magazines Alexandra has now.
    """
    # L1
    friday_magazines = 8 # bought 8 magazines at the bookstore on Friday
    saturday_magazines = 12 # bought 12 more on Saturday
    total_fri_sat = saturday_magazines + friday_magazines

    # L2
    sunday_multiplier = 4 # four times the number of magazines she did on Friday
    sunday_magazines = friday_magazines * sunday_multiplier

    # L3
    total_before_dog = saturday_magazines + friday_magazines + sunday_magazines

    # L4
    dog_chewed = 4 # her dog had chewed up 4 of the magazines
    total_after_dog = total_before_dog - dog_chewed

    # FA
    answer = total_after_dog
    return answer