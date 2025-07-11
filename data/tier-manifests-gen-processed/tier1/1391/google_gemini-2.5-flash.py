def solve():
    """Index: 1391.
    Returns: the total age of all four family members.
    """
    # L1
    susan_age = 15 # Susan is 15 years old
    arthur_age_diff_susan = 2 # Arthur is 2 years older than Susan
    arthur_age = susan_age + arthur_age_diff_susan

    # L2
    bob_age = 11 # Bob is 11 years old
    tom_age_diff_bob = 3 # Tom is 3 years younger than Bob
    tom_age = bob_age - tom_age_diff_bob

    # L3
    total_age = bob_age + susan_age + arthur_age + tom_age

    # FA
    answer = total_age
    return answer