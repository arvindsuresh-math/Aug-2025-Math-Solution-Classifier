def solve_29():
    # Let 'previous_income' be the previous monthly income.

    # Initial rent and utilities cost as a percentage of previous income
    # rent_utilities_cost = 0.40 * previous_income

    # New monthly income after increase
    # new_income = previous_income + 600

    # New rent and utilities cost as a percentage of new income
    # rent_utilities_cost = 0.25 * (previous_income + 600)

    # Since the rent and utilities cost is constant, we can set the two expressions equal:
    # 0.40 * previous_income = 0.25 * (previous_income + 600)

    # Let's solve for previous_income:
    # 0.40 * previous_income = 0.25 * previous_income + 0.25 * 600
    # 0.40 * previous_income = 0.25 * previous_income + 150
    # 0.40 * previous_income - 0.25 * previous_income = 150
    # (0.40 - 0.25) * previous_income = 150
    # 0.15 * previous_income = 150
    # previous_income = 150 / 0.15

    previous_income = 150 / 0.15

    return previous_income

# Execute the function to get the answer
# print(solve_29())