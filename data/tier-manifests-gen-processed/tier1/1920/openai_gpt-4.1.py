def solve():
    """Index: 1920.
    Returns: the number of slices of pizza Blanch has left at the end of the day.
    """
    # L1
    initial_slices = 15 # Blanch has 15 slices of pizza in the fridge
    breakfast_eaten = 4 # she eats 4 slices
    after_breakfast = initial_slices - breakfast_eaten

    # L2
    lunch_eaten = 2 # eats 2 slices at lunch
    after_lunch = after_breakfast - lunch_eaten

    # L3
    snack_eaten = 2 # takes two slices as a snack
    after_snack = after_lunch - snack_eaten

    # L4
    dinner_eaten = 5 # consumes 5 slices for dinner
    after_dinner = after_snack - dinner_eaten

    # FA
    answer = after_dinner
    return answer