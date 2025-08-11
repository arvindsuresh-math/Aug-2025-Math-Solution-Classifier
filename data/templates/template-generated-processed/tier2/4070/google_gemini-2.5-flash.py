def solve():
    """Index: 4070.
    Returns: the total income after paying taxes and buying ingredients.
    """
    # L1
    price_french_fries = 12 # price of French fries is $12
    price_poutine = 8 # price of Poutine is $8
    daily_sales_income = price_french_fries + price_poutine

    # L2
    days_per_week = 7 # WK
    weekly_gross_income = daily_sales_income * days_per_week

    # L3
    tax_rate_decimal = 0.10 # ten percent of his weekly income as tax
    weekly_tax_amount = weekly_gross_income * tax_rate_decimal

    # L4
    income_after_taxes = weekly_gross_income - weekly_tax_amount

    # L5
    daily_ingredient_cost = 10 # spends $10 every day on ingredients
    weekly_ingredient_cost = daily_ingredient_cost * days_per_week

    # L6
    total_weekly_income_after_expenses = income_after_taxes - weekly_ingredient_cost

    # FA
    answer = total_weekly_income_after_expenses
    return answer