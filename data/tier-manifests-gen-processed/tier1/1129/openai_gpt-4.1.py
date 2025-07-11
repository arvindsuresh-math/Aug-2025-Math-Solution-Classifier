def solve():
    """Index: 1129.
    Returns: the total amount of bronze needed for all three bells.
    """
    # L1
    first_bell = 50 # 50 pounds of bronze
    second_bell_multiplier = 2 # twice the size of the first bell
    second_bell = first_bell * second_bell_multiplier

    # L2
    third_bell_multiplier = 4 # four times the size of the second bell
    third_bell = second_bell * third_bell_multiplier

    # L3
    total_bronze = second_bell + third_bell + first_bell

    # FA
    answer = total_bronze
    return answer