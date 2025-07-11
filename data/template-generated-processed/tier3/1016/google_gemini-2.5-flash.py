def solve():
    """Index: 1016.
    Returns: the number of strawberries in the crate.
    """
    # L1
    total_fruit = 78 # 78 pieces of fruit in a crate
    kiwi_denominator = 3 # One-third of the box
    kiwis = total_fruit / kiwi_denominator

    # L2
    strawberries = total_fruit - kiwis

    # FA
    answer = strawberries
    return answer