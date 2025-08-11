def solve():
    """Index: 6898.
    Returns: the total water capacity of the coolers in liters.
    """
    # L1
    first_cooler_capacity = 100 # 100 liters
    second_cooler_bigger_percent = 0.5 # 50% bigger
    second_cooler_increase = first_cooler_capacity * second_cooler_bigger_percent

    # L2
    second_cooler_capacity = first_cooler_capacity + second_cooler_increase

    # L3
    third_cooler_size_factor = 2 # half the size of the second
    third_cooler_capacity = second_cooler_capacity / third_cooler_size_factor

    # L4
    total_capacity = first_cooler_capacity + second_cooler_capacity + third_cooler_capacity

    # FA
    answer = total_capacity
    return answer