def solve():
    """Index: 1129.
    Returns: the total amount of bronze needed for the bells.
    """
    # L1
    first_bell_bronze = 50 # 50 pounds of bronze
    multiplier_second_bell = 2 # twice the size of the first bell
    second_bell_bronze = first_bell_bronze * multiplier_second_bell

    # L2
    multiplier_third_bell = 4 # four times the size of the second bell
    third_bell_bronze = second_bell_bronze * multiplier_third_bell

    # L3
    total_bronze_needed = second_bell_bronze + third_bell_bronze + first_bell_bronze

    # FA
    answer = total_bronze_needed
    return answer