from fractions import Fraction

def solve():
    """Index: 1971.
    Returns: the amount of money each employee is paid monthly.
    """
    # L1
    tax_percentage = Fraction(10, 100) # 10% in taxes
    monthly_revenue = 400000 # revenue of $400000 a month
    taxes_paid = tax_percentage * monthly_revenue

    # L2
    revenue_after_taxes = monthly_revenue - taxes_paid

    # L3
    marketing_percentage = Fraction(5, 100) # 5% of the remaining amount on marketing and ads
    marketing_costs = marketing_percentage * revenue_after_taxes

    # L4
    revenue_after_marketing = revenue_after_taxes - marketing_costs

    # L5
    operational_percentage = Fraction(20, 100) # 20% of the remaining amount on operational costs
    operational_costs = operational_percentage * revenue_after_marketing

    # L6
    revenue_after_operational_costs = revenue_after_marketing - operational_costs

    # L7
    wages_percentage = Fraction(15, 100) # 15% of the remaining amount on employee wages
    total_wages = wages_percentage * revenue_after_operational_costs

    # L8
    num_employees = 10 # 10 employees
    wage_per_employee = total_wages / num_employees

    # FA
    answer = wage_per_employee
    return answer