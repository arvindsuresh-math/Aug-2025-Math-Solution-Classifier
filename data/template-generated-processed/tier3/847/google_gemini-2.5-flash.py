def solve():
    """Index: 847.
    Returns: the selling price per bag to make a 10% profit.
    """
    # L1
    corn_seeds_cost = 50 # spent $50 on corn seeds
    fertilizers_pesticides_cost = 35 # $35 on fertilizers and pesticides
    labor_cost = 15 # $15 on labor
    total_expenditure = corn_seeds_cost + fertilizers_pesticides_cost + labor_cost

    # L2
    profit_percentage_numerator = 10 # profit of 10%
    profit_percentage_denominator = 100 # profit of 10%
    target_sales_revenue = total_expenditure + (total_expenditure * (profit_percentage_numerator / profit_percentage_denominator))

    # L3
    num_bags = 10 # gather 10 bags of corn
    price_per_bag = target_sales_revenue / num_bags

    # FA
    answer = price_per_bag
    return answer