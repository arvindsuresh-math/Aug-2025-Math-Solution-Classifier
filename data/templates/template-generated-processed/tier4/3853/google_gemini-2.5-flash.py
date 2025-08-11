def solve():
    """Index: 3853.
    Returns: the number of slices of cheesecake Kiley ate.
    """
    # L1
    total_calories_cheesecake = 2800 # 2800 calories in every cheesecake
    calories_per_slice = 350 # each slice of cheesecake contains 350 calories
    total_slices_cheesecake = total_calories_cheesecake / calories_per_slice

    # L2
    kiley_ate_percent = 0.25 # Kiley ate 25% of the cheesecake
    slices_kiley_ate = total_slices_cheesecake * kiley_ate_percent

    # FA
    answer = slices_kiley_ate
    return answer