def solve():
    """Index: 4899.
    Returns: the total cost of jelly bracelets in dollars.
    """
    # L5
    jessica_letters = 7 # letters in 'Jessica'
    tori_letters = 4 # letters in 'Tori'
    lily_letters = 4 # letters in 'Lily'
    patrice_letters = 7 # letters in 'Patrice'
    total_letters = jessica_letters + tori_letters + lily_letters + patrice_letters

    # L6
    cost_per_bracelet = 2 # each jelly bracelet costs $2
    total_cost = total_letters * cost_per_bracelet

    # FA
    answer = total_cost
    return answer