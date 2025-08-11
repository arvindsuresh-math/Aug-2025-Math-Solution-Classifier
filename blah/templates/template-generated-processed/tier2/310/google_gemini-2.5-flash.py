def solve():
    """Index: 310.
    Returns: the total amount Janet owes for wages and taxes for one month.
    """
    # L1
    days_per_month = 25 # 25 days a month
    hours_per_day = 8 # 8 hours a day
    hours_per_worker_per_month = days_per_month * hours_per_day

    # L2
    warehouse_worker_hourly_rate = 15 # $15/hour
    warehouse_worker_monthly_wage = hours_per_worker_per_month * warehouse_worker_hourly_rate

    # L3
    num_warehouse_workers = 4 # Four of them are warehouse workers
    total_warehouse_worker_wages = warehouse_worker_monthly_wage * num_warehouse_workers

    # L4
    manager_hourly_rate = 20 # managers who make $20/hour
    manager_monthly_wage = hours_per_worker_per_month * manager_hourly_rate

    # L5
    num_managers = 2 # the other two are managers
    total_manager_wages = manager_monthly_wage * num_managers

    # L6
    total_wages_bill = total_manager_wages + total_warehouse_worker_wages

    # L7
    fica_tax_rate_percent = 10 # 10% of her workers' salaries
    fica_tax_rate_decimal = 0.1 # from solution text: .1
    total_fica_taxes = total_wages_bill * fica_tax_rate_decimal

    # L8
    grand_total_cost = total_fica_taxes + total_wages_bill

    # FA
    answer = grand_total_cost
    return answer