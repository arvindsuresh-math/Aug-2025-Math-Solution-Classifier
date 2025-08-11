def solve():
    """Index: 290.
    Returns: the number of boys who went on the trip.
    """
    # L1
    dozens_prepared = 3 # prepared 3 dozen boiled eggs
    eggs_per_dozen = 12 # WK
    total_eggs = dozens_prepared * eggs_per_dozen

    # L2
    adults = 3 # three adults
    eggs_per_adult = 3 # Every adult got 3 eggs
    eggs_for_adults = adults * eggs_per_adult

    # L3
    eggs_for_children = total_eggs - eggs_for_adults

    # L4
    girls = 7 # number of girls was 7
    eggs_for_boys = eggs_for_children - girls

    # L5
    eggs_per_girl = 1 # each girl received an egg
    extra_eggs_per_boy = 1 # boys each received 1 more egg than each girl
    eggs_per_boy = eggs_per_girl + extra_eggs_per_boy

    # L6
    boys = eggs_for_boys / eggs_per_boy

    # FA
    answer = boys
    return answer