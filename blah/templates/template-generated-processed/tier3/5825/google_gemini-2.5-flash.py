def solve():
    """Index: 5825.
    Returns: the number of tomatoes Thelma needs to feed a family of 8.
    """
    # L1
    slices_per_person = 20 # 20 slices of fried green tomato make a meal for a single person
    family_members = 8 # feed a family of 8
    total_slices_needed = family_members * slices_per_person

    # L2
    slices_per_tomato = 8 # cuts each green tomato into 8 slices
    total_tomatoes_needed = total_slices_needed / slices_per_tomato

    # FA
    answer = total_tomatoes_needed
    return answer