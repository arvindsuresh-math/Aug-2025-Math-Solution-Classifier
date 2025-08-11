def solve():
    """Index: 2309.
    Returns: the company's daily profit from making and selling t-shirts.
    """
    # L1
    shirts_per_employee = 20 # Each person makes on average 20 shirts per day
    pay_per_shirt = 5 # $5 per shirt they make
    shirt_pay = shirts_per_employee * pay_per_shirt

    # L2
    hourly_wage = 12 # $12 an hour
    hours_per_shift = 8 # 8-hour shift
    hourly_pay = hourly_wage * hours_per_shift

    # L3
    total_pay_per_employee = shirt_pay + hourly_pay

    # L4
    num_employees = 20 # hires 20 people
    total_employee_cost = num_employees * total_pay_per_employee

    # L5
    total_shirts = num_employees * shirts_per_employee

    # L6
    price_per_shirt = 35 # sells shirts for $35 each
    total_revenue = total_shirts * price_per_shirt

    # L7
    nonemployee_expenses = 1000 # Nonemployee expenses come out to $1000 a day
    profit = total_revenue - total_employee_cost - nonemployee_expenses

    # FA
    answer = profit
    return answer