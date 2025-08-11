def solve():
    """Index: 5759.
    Returns: the total number of letters in Jonathan's and his sister's names.
    """
    # L1
    jonathan_first_name_letters = 8 # 8 letters for the first name
    jonathan_surname_letters = 10 # 10 letters for the surname
    jonathan_total_letters = jonathan_first_name_letters + jonathan_surname_letters

    # L2
    sister_first_name_letters = 5 # 5 letters for the first name
    sister_second_name_letters = 10 # 10 letters for the second name
    sister_total_letters = sister_first_name_letters + sister_second_name_letters

    # L3
    total_letters_combined = jonathan_total_letters + sister_total_letters

    # FA
    answer = total_letters_combined
    return answer