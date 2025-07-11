def solve():
    """Index: 741.
    Returns: Justin's current age.
    """
    # L1
    angelina_future_years = 5 # In 5 years
    angelina_future_age = 40 # Angelina will be 40 years old
    angelina_current_age = angelina_future_age - angelina_future_years

    # L2
    angelina_older_by = 4 # Angelina is 4 years older than Justin
    justin_current_age = angelina_current_age - angelina_older_by

    # FA
    answer = justin_current_age
    return answer