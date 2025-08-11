def solve():
    """Index: 5026.
    Returns: the average amount of fish caught per person.
    """
    # L1
    aang_fish = 7 # Aang caught 7 fish
    sokka_fish = 5 # Sokka caught 5 fish
    toph_fish = 12 # Toph caught 12 fish
    total_fish_caught = aang_fish + sokka_fish + toph_fish

    # L2
    number_of_people = 3 # Aang, Sokka, and Toph are 3 people
    average_fish_per_person = total_fish_caught / number_of_people

    # FA
    answer = average_fish_per_person
    return answer