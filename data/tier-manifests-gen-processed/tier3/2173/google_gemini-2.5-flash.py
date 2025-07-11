def solve():
    """Index: 2173.
    Returns: the number of people who sat at each table.
    """
    # L1
    kids = 45 # 45 kids
    adults = 123 # 123 adults
    total_people = kids + adults

    # L2
    tables = 14 # 14 tables
    people_per_table = total_people / tables

    # FA
    answer = people_per_table
    return answer