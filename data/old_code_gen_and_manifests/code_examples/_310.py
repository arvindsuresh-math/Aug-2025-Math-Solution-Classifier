def solve(
        num_employees: int = 6, # Janet hires six employees
        num_warehouse_workers: int = 4, # Four of them are warehouse workers
        num_managers: int = 2, # the other two are managers
        hourly_wage_warehouse: int = 15, # warehouse workers make $15/hour
        hourly_wage_manager: int = 20, # managers make $20/hour
        fica_tax_rate: float = 0.1, # FICA tax rate is 10%
        days_per_month: int = 25, # everyone works 25 days a month
        hours_per_day: int = 8 # everyone works 8 hours a day
    ):
    """Index: 310.
    Returns: the monthly total wage bill, including FICA taxes.
    """
    #: L1
    hours_per_month = days_per_month * hours_per_day

    #: L2
    monthly_wage_warehouse = hourly_wage_warehouse * hours_per_month

    #: L3
    total_wage_warehouse = monthly_wage_warehouse * num_warehouse_workers

    #: L4
    monthly_wage_manager = hourly_wage_manager * hours_per_month

    #: L5
    total_wage_manager = monthly_wage_manager * num_managers

    #: L6
    total_wages = total_wage_warehouse + total_wage_manager

    #: L7
    fica_taxes = total_wages * fica_tax_rate

    #: L8
    grand_total = total_wages + fica_taxes

    answer = grand_total # FINAL ANSWER
    return answer