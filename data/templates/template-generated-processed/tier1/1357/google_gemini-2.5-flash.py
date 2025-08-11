def solve():
    """Index: 1357.
    Returns: the total number of cents Lizzy has now.
    """
    # L1
    mother_gave = 80 # gave her 80 cents
    father_gave = 40 # gave her 40 cents
    initial_total_from_parents = mother_gave + father_gave

    # L2
    spent_on_candy = 50 # spent 50 cents buying candy
    after_spending = initial_total_from_parents - spent_on_candy

    # L3
    uncle_gave = 70 # Her uncle gave her another 70 cents
    final_total = after_spending + uncle_gave

    # FA
    answer = final_total
    return answer