def solve():
    """Index: 310.
    Returns: the total amount Janet owes for wages and taxes for one month.
    """
    # L1
    days_per_month = 25 # works 25 days a month
    hours_per_day = 8 # and 8 hours a day
    hours_per_worker_per_month = days_per_month * hours_per_day

    # L2
    warehouse_worker_wage = 15 # make $15/hour
    wage_per_warehouse_worker = hours_per_worker_per_month * warehouse_worker_wage

    # L3
    num_warehouse_workers = 4 # Four of them are warehouse workers
    total_warehouse_wages = wage_per_warehouse_worker * num_warehouse_workers

    # L4
    manager_wage = 20 # make $20/hour
    wage_per_manager = hours_per_worker_per_month * manager_wage

    # L5
    num_managers = 2 # the other two are managers
    total_manager_wages = wage_per_manager * num_managers

    # L6
    total_wages = total_manager_wages + total_warehouse_wages

    # L7
    fica_tax_rate = 0.1 # pay 10% of her workers' salaries in FICA taxes
    fica_taxes = total_wages * fica_tax_rate

    # L8
    grand_total = total_wages + fica_taxes

    # FA
    answer = grand_total
    return answer