def solve():
    """Index: 1357.
    Returns: the number of cents Lizzy has now.
    """
    # L1
    mother_gave = 80 # Lizzy's mother gave her 80 cents
    father_gave = 40 # her father gave her 40 cents
    total_from_parents = mother_gave + father_gave

    # L2
    spent_on_candy = 50 # spent 50 cents buying candy
    after_spending = total_from_parents - spent_on_candy

    # L3
    uncle_gave = 70 # her uncle gave her another 70 cents
    total_cents = after_spending + uncle_gave

    # FA
    answer = total_cents
    return answer