def solve():
    """Index: 3666.
    Returns: the age of Jordan's dog, Max, on Aubrey's 8th birthday.
    """
    # L1
    aubrey_birthday_age = 8 # On Aubrey's 8th birthday
    luka_age_difference = 2 # 2 years older than is Aubrey
    luka_age_on_aubrey_birthday = aubrey_birthday_age + luka_age_difference

    # L2
    luka_age_when_max_born = 4 # Luka turned 4 years old
    max_age_on_aubrey_birthday = luka_age_on_aubrey_birthday - luka_age_when_max_born

    # FA
    answer = max_age_on_aubrey_birthday
    return answer