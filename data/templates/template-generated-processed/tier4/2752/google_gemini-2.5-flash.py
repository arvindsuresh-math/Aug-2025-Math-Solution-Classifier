def solve():
    """Index: 2752.
    Returns: the amount left of the annual budget.
    """
    # L1
    library_spent = 3000 # Centerville spent $3,000 on its public library
    library_budget_percent = 0.15 # 15% of its annual budget on its public library
    total_budget = library_spent / library_budget_percent

    # L2
    parks_budget_percent = 0.24 # 24% on the public parks
    parks_budget = total_budget * parks_budget_percent

    # L3
    remaining_budget = total_budget - (library_spent + parks_budget)

    # FA
    answer = remaining_budget
    return answer