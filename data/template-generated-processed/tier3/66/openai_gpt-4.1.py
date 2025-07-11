def solve():
    """Index: 66.
    Returns: Tara's remaining balance after paying for 4 months.
    """
    # L1
    laptop_cost = 1000 # laptop which costs $1000
    down_payment_percentage_numerator = 20 # 20% down payment
    down_payment_percentage_denominator = 100 # 20% down payment
    required_down_payment = laptop_cost * down_payment_percentage_numerator / down_payment_percentage_denominator

    # L2
    additional_down_payment = 20 # Tara wants to pay an additional $20
    total_down_payment = required_down_payment + additional_down_payment

    # L3
    remaining_balance = laptop_cost - total_down_payment

    # L4
    months_per_year = 12 # WK
    monthly_payment = remaining_balance / months_per_year

    # L5
    months_paid = 4 # paying for 4 months
    total_paid_in_4_months = monthly_payment * months_paid

    # L6
    answer = remaining_balance - total_paid_in_4_months
    return answer