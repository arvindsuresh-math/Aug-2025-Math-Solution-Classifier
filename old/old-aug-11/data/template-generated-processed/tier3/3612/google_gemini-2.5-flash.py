def solve():
    """Index: 3612.
    Returns: the total amount Carl spent on index cards.
    """
    # L1
    students_per_class = 30 # each class has 30 students
    periods_per_day = 6 # He teaches 6 periods a day
    total_students = students_per_class * periods_per_day

    # L2
    cards_per_student = 10 # He gives each student 10 index cards
    total_cards_needed = total_students * cards_per_student

    # L3
    cards_per_pack = 50 # a 50 pack of index cards
    total_packs_needed = total_cards_needed / cards_per_pack

    # L4
    cost_per_pack = 3 # cost $3
    total_cost = total_packs_needed * cost_per_pack

    # FA
    answer = total_cost
    return answer