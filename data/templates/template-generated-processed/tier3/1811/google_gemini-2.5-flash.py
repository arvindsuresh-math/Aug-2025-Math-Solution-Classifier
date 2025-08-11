def solve():
    """Index: 1811.
    Returns: the number of supplies Kelly has left.
    """
    # L1
    num_students = 8 # She has 8 students
    paper_per_student = 3 # they will need 3 pieces of construction paper each
    initial_construction_paper = num_students * paper_per_student

    # L2
    num_glue_bottles = 6 # she needs to buy 6 bottles of glue
    supplies_before_drop = initial_construction_paper + num_glue_bottles

    # L3
    drop_divisor = 2 # dropped half of them
    supplies_after_drop = supplies_before_drop / drop_divisor

    # L4
    additional_paper = 5 # buy 5 more pieces of construction paper
    final_supplies = supplies_after_drop + additional_paper

    # FA
    answer = final_supplies
    return answer