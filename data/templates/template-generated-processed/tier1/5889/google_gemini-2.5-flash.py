def solve():
    """Index: 5889.
    Returns: the number of years Aziz's parents had been living in America before Aziz was born.
    """
    # L1
    current_year = 2021 # The year is 2021
    aziz_age = 36 # Aziz just celebrated his 36th birthday
    aziz_birth_year = current_year - aziz_age

    # L2
    parents_moved_year = 1982 # Aziz's parents moved to America in 1982
    years_before_aziz_born = aziz_birth_year - parents_moved_year

    # FA
    answer = years_before_aziz_born
    return answer