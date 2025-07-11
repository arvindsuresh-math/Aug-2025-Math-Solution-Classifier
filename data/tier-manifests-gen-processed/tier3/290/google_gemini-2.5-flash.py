def solve():
    """Index: 290.
    Returns: the number of boys who went on the trip.
    """
    # L1
    num_dozens = 3 # prepared 3 dozen boiled eggs
    eggs_per_dozen = 12 # WK
    total_eggs = num_dozens * eggs_per_dozen

    # L2
    num_adults = 3 # three adults
    eggs_per_adult = 3 # Every adult got 3 eggs
    adult_eggs = num_adults * eggs_per_adult

    # L3
    children_eggs = total_eggs - adult_eggs

    # L4
    num_girls = 7 # the number of girls was 7
    eggs_per_girl = 1 # each girl received an egg
    boys_eggs = children_eggs - num_girls

    # L5
    extra_egg_for_boy = 1 # 1 more egg than each girl
    eggs_per_boy = extra_egg_for_boy + eggs_per_girl

    # L6
    num_boys = boys_eggs / eggs_per_boy

    # FA
    answer = num_boys
    return answer