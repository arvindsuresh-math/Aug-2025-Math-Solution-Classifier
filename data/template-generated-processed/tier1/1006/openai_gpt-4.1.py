def solve():
    """Index: 1006.
    Returns: Jayson's mom's age when he was born.
    """
    # L1
    jayson_age = 10 # When Jayson is 10
    dad_times_jayson = 4 # dad is four times his age
    dad_age = jayson_age * dad_times_jayson

    # L2
    mom_younger_than_dad = 2 # mom is 2 years younger than his dad
    mom_age = dad_age - mom_younger_than_dad

    # L3
    mom_age_when_jayson_born = mom_age - jayson_age

    # FA
    answer = mom_age_when_jayson_born
    return answer