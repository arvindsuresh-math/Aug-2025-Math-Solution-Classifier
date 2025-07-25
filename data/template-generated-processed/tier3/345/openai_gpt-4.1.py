def solve():
    """Index: 345.
    Returns: the total amount Adam earns after taxes in 30 days.
    """
    # L1
    daily_pay = 40 # Adam earns $40 daily in his job
    tax_divisor = 10 # 10% of his money is deducted as taxes
    daily_tax = daily_pay / tax_divisor

    # L2
    daily_after_tax = daily_pay - daily_tax

    # L3
    num_days = 30 # after 30 days of work
    total_after_tax = daily_after_tax * num_days

    # FA
    answer = total_after_tax
    return answer