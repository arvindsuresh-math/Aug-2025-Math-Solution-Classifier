def solve(
        num_employees: int = 6, # Janet hires six employees
        num_warehouse_workers: int = 4, # four of them are warehouse workers
        num_managers: int = 2, # the other two are managers
        hourly_wage_warehouse: int = 15, # warehouse workers make $15/hour
        hourly_wage_manager: int = 20, # managers make $20/hour
        fica_tax_rate: float = 0.1, # FICA tax rate is 10%
        days_per_month: int = 25, # each worker works 25 days a month
        hours_per_day: int = 8 # each worker works 8 hours a day
    ):
    """Code for Q 310 from the GSM8K dataset (train).
    Returns the monthly total wage bill, including FICA taxes.
    """
    # First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    hours_per_month = days_per_month * hours_per_day

    # Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    monthly_wage_warehouse = hourly_wage_warehouse * hours_per_month

    # Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12,000
    total_wage_warehouse = monthly_wage_warehouse * num_warehouse_workers

    # Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4,000
    monthly_wage_manager = hourly_wage_manager * hours_per_month

    # Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4,000/manager * 2 managers = $<<4000*2=8000>>8,000
    total_wage_manager = monthly_wage_manager * num_managers

    # Now add the wages for the managers and the workers to find the total cost of the wages: $8,000 + $12,000 = $<<8000+12000=20000>>20,000
    total_wages = total_wage_warehouse + total_wage_manager

    # Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20,000 * .1 = $<<20000*.1=2000>>2,000
    fica_taxes = total_wages * fica_tax_rate

    # Now add the total wage bill to the total tax amount to find the grand total: $20,000 + $2,000 = $<<20000+2000=22000>>22,000
    grand_total = total_wages + fica_taxes

    # The final answer is the grand total
    return grand_total