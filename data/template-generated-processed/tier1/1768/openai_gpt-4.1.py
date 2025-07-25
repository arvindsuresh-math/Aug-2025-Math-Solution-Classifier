def solve():
    """Index: 1768.
    Returns: the number of cats Jeff currently has in his shelter.
    """
    # L1
    initial_cats = 20 # currently takes care of 20 cats
    kittens_found = 2 # found 2 kittens in a box
    injured_cat = 1 # found 1 more cat with a leg injury
    total_cats_before_adoption = initial_cats + kittens_found + injured_cat

    # L2
    people_adopted = 3 # 3 people adopted
    cats_per_person = 2 # 2 cats each
    total_cats_adopted = people_adopted * cats_per_person

    # L3
    cats_remaining = total_cats_before_adoption - total_cats_adopted

    # FA
    answer = cats_remaining
    return answer