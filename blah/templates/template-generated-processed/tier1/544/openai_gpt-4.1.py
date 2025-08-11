def solve():
    """Index: 544.
    Returns: the number of kilograms of dog food Elise already had.
    """
    # L1
    first_bag_kg = 15 # 15kg bag
    second_bag_kg = 10 # another 10kg bag
    total_bought = first_bag_kg + second_bag_kg

    # L2
    total_now = 40 # she now has 40kg of dog food
    already_had = total_now - total_bought

    # FA
    answer = already_had
    return answer