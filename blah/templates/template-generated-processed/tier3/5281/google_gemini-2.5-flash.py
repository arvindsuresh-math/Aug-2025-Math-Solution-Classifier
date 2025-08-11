def solve():
    """Index: 5281.
    Returns: the amount of money each child receives.
    """
    # L1
    husband_weekly_savings = 335 # The husband gives $335 every week
    weeks_per_month = 4 # assume 4 weeks in each month
    husband_monthly_savings = husband_weekly_savings * weeks_per_month

    # L2
    wife_weekly_savings = 225 # the wife gives $225 every week
    wife_monthly_savings = wife_weekly_savings * weeks_per_month

    # L3
    couple_monthly_savings = husband_monthly_savings + wife_monthly_savings

    # L4
    saving_months = 6 # After 6 months of saving
    total_savings = couple_monthly_savings * saving_months

    # L5
    division_factor_half = 2 # divide half of the couple's savings
    half_savings = total_savings / division_factor_half

    # L6
    number_of_children = 4 # into their four children's savings accounts
    each_child_receives = half_savings / number_of_children

    # FA
    answer = each_child_receives
    return answer