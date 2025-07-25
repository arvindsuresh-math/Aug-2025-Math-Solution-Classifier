def solve():
    """Index: 3951.
    Returns: the current age of Kelsey's older sister.
    """
    # L1
    kelsey_age_1999 = 25 # Kelsey turned 25 in 1999
    year_kelsey_turned_25 = 1999 # Kelsey turned 25 in 1999
    kelsey_birth_year = year_kelsey_turned_25 - kelsey_age_1999

    # L2
    sister_older_by_years = 3 # Her older sister was born 3 years before Kelsey
    sister_birth_year = kelsey_birth_year - sister_older_by_years

    # L3
    current_year = 2021 # It's currently 2021
    sister_current_age = current_year - sister_birth_year

    # FA
    answer = sister_current_age
    return answer