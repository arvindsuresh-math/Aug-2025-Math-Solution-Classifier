def solve():
    """Index: 1192.
    Returns: the number of children who attended the party.
    """
    # L1
    total_people = 120 # 120 people who attended the party
    men_fraction_denominator = 3 # 1/3 are men
    men_at_party = total_people / men_fraction_denominator

    # L2
    women_fraction_denominator = 2 # half are women
    women_at_party = total_people / women_fraction_denominator

    # L3
    total_men_and_women = men_at_party + women_at_party

    # L4
    children_at_party = total_people - total_men_and_women

    # FA
    answer = children_at_party
    return answer