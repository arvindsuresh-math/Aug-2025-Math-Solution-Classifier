def solve():
    """Index: 4657.
    Returns: the total amount of cloth Fatima will have donated.
    """
    # L1
    initial_cloth_size = 100 # 100 square inches big
    cut_divisor = 2 # cut the cloth in half
    first_cut_size = initial_cloth_size / cut_divisor

    # L2
    second_cut_size = first_cut_size / cut_divisor

    # L3
    total_donated_cloth = first_cut_size + second_cut_size

    # FA
    answer = total_donated_cloth
    return answer