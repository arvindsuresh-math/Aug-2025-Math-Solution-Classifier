def solve():
    """Index: 6669.
    Returns: the total amount Jackson spends on school supplies.
    """
    # L1
    pens_per_student = 5 # Each student needs 5 pens
    cost_per_pen = 0.50 # Pens cost $0.50
    cost_pens_per_student = pens_per_student * cost_per_pen

    # L2
    notebooks_per_student = 3 # Each student needs 3 notebooks
    cost_per_notebook = 1.25 # notebooks cost $1.25
    cost_notebooks_per_student = notebooks_per_student * cost_per_notebook

    # L3
    highlighters_per_student = 2 # Each student needs 2 highlighters
    cost_per_highlighter = 0.75 # highlighters cost $0.75
    cost_highlighters_per_student = highlighters_per_student * cost_per_highlighter

    # L4
    cost_per_binder = 4.25 # 1 binder and binders cost $4.25
    total_cost_per_student = cost_pens_per_student + cost_notebooks_per_student + cost_highlighters_per_student + cost_per_binder

    # L5
    num_students = 30 # which has 30 students
    total_cost_before_discount = num_students * total_cost_per_student

    # L6
    teacher_discount = 100.00 # gets a $100 teacher discount
    final_cost = total_cost_before_discount - teacher_discount

    # FA
    answer = final_cost
    return answer