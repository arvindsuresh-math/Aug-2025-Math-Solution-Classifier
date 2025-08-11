def solve():
    """Index: 5273.
    Returns: the total number of pages Sarah will copy.
    """
    # L1
    copies_per_person = 2 # 2 copies of a contract
    num_people = 9 # 9 people
    total_copies_needed = copies_per_person * num_people

    # L2
    pages_per_contract = 20 # 20 pages long
    total_pages_to_copy = pages_per_contract * total_copies_needed

    # FA
    answer = total_pages_to_copy
    return answer