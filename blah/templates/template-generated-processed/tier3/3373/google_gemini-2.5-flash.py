def solve():
    """Index: 3373.
    Returns: the number of Easter eggs each person gets.
    """
    # L1
    num_baskets = 15 # 15 Easter egg baskets
    eggs_per_basket = 12 # 12 Easter eggs
    total_eggs = num_baskets * eggs_per_basket

    # L2
    other_adults = 7 # 7 other adults
    shonda = 1 # Shonda (1)
    shondas_kids = 2 # 2 kids
    friends = 10 # 10 friends
    total_people = other_adults + shonda + shondas_kids + friends

    # L3
    eggs_per_person = total_eggs / total_people

    # FA
    answer = eggs_per_person
    return answer