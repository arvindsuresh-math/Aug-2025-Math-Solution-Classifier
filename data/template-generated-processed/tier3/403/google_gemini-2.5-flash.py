def solve():
    """Index: 403.
    Returns: the average age of the three people.
    """
    # L1
    kimiko_age = 28 # Kimiko is 28 years old
    omi_multiplier = 2 # Omi is twice as old as Kimiko
    omi_age = omi_multiplier * kimiko_age

    # L2
    arlette_fraction_numerator = 3 # Arlette is 3/4 times as old as Kimiko
    arlette_fraction_denominator = 4 # Arlette is 3/4 times as old as Kimiko
    arlette_age = (arlette_fraction_numerator / arlette_fraction_denominator) * kimiko_age

    # L3
    total_age = arlette_age + omi_age + kimiko_age

    # L4
    number_of_people = 3 # average age of the three
    average_age = total_age / number_of_people

    # FA
    answer = average_age
    return answer