def solve():
    """Index: 6974.
    Returns: the number of days five loaves of bread will last.
    """
    # L1
    breakfast_slices = 3 # 3 slices of bread during breakfast
    snack_slices = 2 # 2 slices of bread for snacks
    daily_slices_per_member = breakfast_slices + snack_slices

    # L2
    num_members = 4 # four members in one household
    daily_family_consumption = daily_slices_per_member * num_members

    # L3
    num_loaves = 5 # five loaves of bread
    slices_per_loaf = 12 # A loaf of bread has 12 slices
    total_slices_available = num_loaves * slices_per_loaf

    # L4
    days_lasted = total_slices_available / daily_family_consumption

    # FA
    answer = days_lasted
    return answer